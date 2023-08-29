import pandas as pd
from mongodb_connector import connect_to_mongodb, save_cluster_centers_to_mongodb
from kmeans_algorithm import kmeans

if __name__ == "__main__":
    # Thiết lập thông tin kết nối MongoDB
    mongodb_uri = "mongodb://localhost:27017/"
    database_name = "data-mining"
    collection_name = "patients"
    
    try:
        # Kết nối tới MongoDB và lấy dữ liệu
        collection = connect_to_mongodb(mongodb_uri, database_name, collection_name)
        data_from_mongodb = list(collection.find())
        data = pd.DataFrame(data_from_mongodb)
        data = data.drop(columns=['_id'])
        data.info()
        
        # Số lượng cụm bạn muốn tạo
        num_clusters = 3
        centers = kmeans(num_clusters, data)

        # Lưu các tâm cụm vào MongoDB
        save_cluster_centers_to_mongodb(centers, mongodb_uri, database_name)
    except:
        print('Không thể kết nối tới dữ liệu.')