import random
import pandas as pd

def generate_data(num_records):
    data = []

    for _ in range(num_records):
        age = random.randint(18, 90)
        gender = random.choice([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, ''])
        chest_pain_type = random.choice([1, 2, 3, 4])
        blood_pressure = random.choice([random.randint(0, 40), random.randint(200, 300), random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), 
                                        random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), 
                                        random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), random.randint(90, 180), random.randint(90, 180)])
        cholesterol = random.randint(120, 300)
        max_heart_rate = random.randint(70, 220)
        exercise_angina = random.choice([0, 1])
        plasma_glucose = random.choice([random.randint(70, 250), random.randint(70, 250), random.randint(70, 250), 
                                        random.randint(70, 250), random.randint(70, 250), random.randint(70, 250),  
                                        random.randint(70, 250), random.randint(70, 250), random.randint(70, 250), ''])
        skin_thickness = random.choice([random.randint(20, 100), random.randint(20, 100), random.randint(20, 100),
                                        random.randint(20, 100), random.randint(20, 100), random.randint(20, 100),
                                        random.randint(20, 100), random.randint(20, 100), random.randint(20, 100), ''])
        insulin = random.choice([random.randint(80, 180), random.randint(80, 180), random.randint(80, 180),
                                 random.randint(80, 180), random.randint(80, 180), random.randint(80, 180),
                                 random.randint(80, 180), random.randint(80, 180), random.randint(80, 180), ''])
        bmi = random.uniform(10.0, 50.0)
        diabetes_pedigree = random.uniform(0.1, 2.5)
        hypertension = random.choice([0, 1])
        heart_disease = random.choice([0, 1])
        residence_type = random.choice(['Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Rural', 'Urban', 'Rural', ''])
        smoking_status = random.choice(['Smoker', 'Non-Smoker', 'Smoker', 'Non-Smoker', 'Smoker', 'Non-Smoker', 'Smoker', 'Non-Smoker', 'Smoker', 'Non-Smoker', 'Smoker', 'Non-Smoker', 'Unknown'])

        data.append([age, gender, chest_pain_type, blood_pressure, cholesterol, max_heart_rate,
                     exercise_angina, plasma_glucose, skin_thickness, insulin, bmi, diabetes_pedigree,
                     hypertension, heart_disease, residence_type, smoking_status])

    return data

def write_to_csv(data):
    headers = ['age', 'gender', 'chest_pain_type', 'blood_pressure', 'cholesterol', 'max_heart_rate',
               'exercise_angina', 'plasma_glucose', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree',
               'hypertension', 'heart_disease', 'residence_type', 'smoking_status']

    df = pd.DataFrame(data, columns=headers)
    df.to_csv('patient_dataset.csv', index=False)

def main():
    num_records = 6000
    data = generate_data(num_records)
    write_to_csv(data)
    print(f"Successfully generated {num_records} patient records and saved to 'patient_data.csv'.")

if __name__ == "__main__":
    main()
