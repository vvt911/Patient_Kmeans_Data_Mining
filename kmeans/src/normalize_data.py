import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Tạo một đối tượng LabelEncoder
label_encoder = LabelEncoder()

# Đọc dữ liệu từ file CSV
data = pd.read_csv('patient_raw.csv')
print(data.info())

# Xóa các cột 'gender', 'skin_thickness' và 'residence_type', 'diabetes_pedigree'
columns_to_drop = ['gender', 'skin_thickness', 'residence_type', 'diabetes_pedigree']
data = data.drop(columns=columns_to_drop)

# Sử dụng LabelEncoder cho cột 'smoking_status'
label_mapping = {
    'never smoked': 0,
    'formerly smoked': 1,
    'Unknown': 2,
    'smokes': 3
}
label_encoder = LabelEncoder()
data['smoking_status'] = data['smoking_status'].map(label_mapping)

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

# Chuẩn hóa Min-Max Scaling cho các thuộc tính
columns_to_scale = ['age', 'blood_pressure', 'cholesterol', 'max_heart_rate', 'plasma_glucose', 
                    'insulin', 'bmi']
data[columns_to_scale] = ((data[columns_to_scale] - data[columns_to_scale].min()) / 
                         (data[columns_to_scale].max() - data[columns_to_scale].min()))

# Lưu dữ liệu đã chuẩn hóa vào một file mới
data.to_csv("patient_normalization.csv", index=False)
print(data.info())
print("Dữ liệu đã chuẩn hóa đã được lưu vào file 'patient_normalization.csv'")