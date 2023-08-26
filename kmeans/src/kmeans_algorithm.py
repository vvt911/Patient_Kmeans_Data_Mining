import pandas as pd
import numpy as np
from mongodb_connector import connect_to_mongodb, save_cluster_centers_to_mongodb

# Hàm tính khoảng cách giữa các điểm và trung tâm cụm
def distance(x, centers):
    return np.linalg.norm(x - centers, axis=1)

# Tạo bảng thông tin chi tiết về từng cụm
def cluster_info(num_clusters, data):
    cluster_summary = pd.DataFrame()
    cluster_summary['Attribute'] = data.columns.drop('cluster')
    cluster_summary.set_index('Attribute', inplace=True)

    # Tính giá trị trung bình của các thuộc tính trong từng cụm
    for i in range(num_clusters):
        cluster_data = data[data['cluster'] == i].drop(columns=['cluster'])
        cluster_summary[f'Cluster {i}'] = cluster_data.mean()

    # Thêm cột tổng cộng của toàn bộ dữ liệu
    cluster_summary['Full Data'] = data.drop(columns=['cluster']).mean()

    # Hiển thị bảng thông tin chi tiết
    print("\nFinal cluster centroids:")
    print(cluster_summary)

    # Số lượng bệnh nhân trong mỗi cụm
    cluster_counts = data['cluster'].value_counts()

    print("===========================================================")
    print("\nSố lượng bệnh nhân trong mỗi cụm:")
    for cluster_id, cluster_count in cluster_counts.items():
        print(f"Cụm {cluster_id}: {cluster_count} bệnh nhân ({cluster_count / len(data) * 100:.2f}%)")


def kmeans(num_clusters, data):
    # Lấy tên cột và chuyển đổi data từ pandas => numpy
    columns_name = data.columns
    data = data.values
    # Khởi tạo các tâm cụm ban đầu ngẫu nhiên
    np.random.seed(42)
    initial_centers_idx = np.random.choice(data.shape[0], size=num_clusters, replace=False)
    initial_centers = data[initial_centers_idx]

    np.set_printoptions(precision=5, suppress=True)
    print("===========================================================")
    print("Ba tâm cụm ban đầu:")
    for i, initial_center in enumerate(initial_centers):
        center_str = ', '.join(format(x, '.5f') for x in initial_center)
        print(f"Cluster center {i}: {center_str}")

    # Áp dụng thuật toán KMeans để phân cụm dữ liệu
    max_iters = 100
    tolerance = 1e-10
    centers = initial_centers
    for iteration in range(max_iters):
        # Gán mỗi điểm vào cụm gần nhất
        labels = np.argmin(np.apply_along_axis(
            lambda x: distance(x, centers), axis=1, arr=data), axis=1)
        
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
    
    print("\nSố lần lặp:", iteration + 1)

    data = pd.DataFrame(data, columns=columns_name)
    data['cluster'] = labels

    # Hiển thị thông tin các cụm sau khi hoàn thành
    cluster_info(num_clusters, data)
    return centers
