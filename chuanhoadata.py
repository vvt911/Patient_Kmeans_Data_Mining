import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Tạo một đối tượng LabelEncoder
label_encoder = LabelEncoder()

# Đọc dữ liệu từ file CSV
data = pd.read_csv('patient_priority.csv')
print(data.info())

# Xóa các cột 'gender', 'skin_thickness' và 'residence_type'
columns_to_drop = ['gender', 'skin_thickness', 'residence_type', 'diabetes_pedigree']
data = data.drop(columns=columns_to_drop)

# Sử dụng LabelEncoder cho cột 'smoking_status'
label_encoder = LabelEncoder()
data['smoking_status'] = label_encoder.fit_transform(data['smoking_status'])

# Chỉ định danh sách các cột cần điền giá trị thiếu
numeric_columns_float = ['plasma_glucose', 'bmi']
data[numeric_columns_float] = data[numeric_columns_float].fillna(data[numeric_columns_float].mean())

numeric_columns_int = [
    'age', 'chest_pain_type', 'blood_pressure', 'cholesterol', 
    'max_heart_rate', 'insulin'
]
data[numeric_columns_int] = data[numeric_columns_int].fillna(data[numeric_columns_int].mean().round())

# Loại bỏ các bản ghi có blood_pressure nhỏ hơn 90 hoặc lớn hơn 180
data = data[(data['blood_pressure'] >= 90) & (data['blood_pressure'] <= 180)]

numeric_columns = ['chest_pain_type', 'exercise_angina', 'hypertension', 'heart_disease', 'smoking_status']
data[numeric_columns].fillna(data[numeric_columns].mode().iloc[0], inplace=True)

# # Chọn các đặc trưng để thực hiện phân cụm
# columns_name = [
#     'age', 'chest_pain_type', 'blood_pressure', 'cholesterol', 'max_heart_rate',
#     'exercise_angina', 'plasma_glucose', 'insulin', 'bmi',
#     'hypertension', 'heart_disease', 'smoking_status'
# ]

# # Tạo DataFrame từ dữ liệu và tên cột
# data = pd.DataFrame(data, columns=columns_name)

# Lưu dữ liệu đã chuẩn hóa vào một file mới
data.to_csv("patient_dataset_normalization.csv", index=False)
print(data.info())
print("Dữ liệu đã chuẩn hóa đã được lưu vào file 'patient_dataset_normalization.csv'")