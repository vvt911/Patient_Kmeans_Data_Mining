import pymongo

def connect_to_mongodb(uri, database_name, collection_name):
    client = pymongo.MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]
    return collection


def save_cluster_centers_to_mongodb(centers, mongodb_uri, database_name):
    final_cluster_centers = []
    for i, center in enumerate(centers):
        final_cluster_centers.append({'cluster_id': i, 'center': center.tolist()})
        
    collection = connect_to_mongodb(mongodb_uri, database_name, "centroids")
    collection.delete_many({})
    fields = ["age", "chest_pain_type", "blood_pressure", "cholesterol", "max_heart_rate", 
            "exercise_angina", "plasma_glucose", "insulin", "bmi", "hypertension", "heart_disease", "smoking_status"]

    for i, center in enumerate(final_cluster_centers):
        data = {field: center['center'][idx] for idx, field in enumerate(fields)}
        data['cluster'] = center['cluster_id']
        collection.insert_one(data)
