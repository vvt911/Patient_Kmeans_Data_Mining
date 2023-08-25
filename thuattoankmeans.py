import pandas as pd
import numpy as np

data = pd.read_csv('patient_dataset_normalization.csv')
print(data.info())
columns_name = data.columns
data = data.values

# Hàm tính khoảng cách giữa các điểm và trung tâm cụm
def distance(x, centers):
    return np.linalg.norm(x - centers, axis=1)

# Số lượng cụm bạn muốn tạo
num_clusters = 3

# Khởi tạo các trung tâm cụm ban đầu ngẫu nhiên
np.random.seed(42)
initial_centers_idx = np.random.choice(data.shape[0], size=num_clusters, replace=False)
initial_centers = data[initial_centers_idx]

np.set_printoptions(precision=5, suppress=True)
print("Ba tâm cụm ban đầu:")
print(initial_centers)

# Áp dụng thuật toán KMeans để phân cụm dữ liệu
max_iters = 100
tolerance = 1e-4
centers = initial_centers

for _ in range(max_iters):
    # Gán mỗi điểm vào cụm gần nhất
    labels = np.argmin(np.apply_along_axis(lambda x: distance(x, centers), axis=1, arr=data), axis=1)
    
    # Lưu trữ trung tâm cũ để so sánh sau
    old_centers = centers.copy()
    
    # Cập nhật trung tâm cụm
    for i in range(num_clusters):
        cluster_points = data[labels == i]
        if len(cluster_points) > 0:
            centers[i] = np.mean(cluster_points, axis=0)
    
    # Kiểm tra điều kiện dừng
    if np.linalg.norm(centers - old_centers) < tolerance:
        break

print("Ba tâm cụm cuối cùng:")
print(centers)

data = pd.DataFrame(data, columns=columns_name)
# Gán nhãn cụm cho dữ liệu
data['cluster'] = labels

# In thông tin về số lượng bệnh nhân trong mỗi cụm
print(data['cluster'].value_counts())