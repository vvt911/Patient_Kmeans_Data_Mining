document.addEventListener("DOMContentLoaded", function () {
    let chartVisible = false;
    let newChart = null;

    document.getElementById("show-centroids").addEventListener("click", async function (event) {
        if (chartVisible) {
            document.getElementsByClassName('chartCard')[0].classList.add("d-none");
            if (newChart) {
                newChart.destroy();
                newChart = null;
            }
            chartVisible = false;
            return;
        }
        try {
            const response = await fetch("http://127.0.0.1:3000/api/centroids", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            if (response.ok) {
                const centroidsData = await response.json();
                const labels = [];
                const data = [];
                const datasets = [];
                const labels_column = [];
                const color_column = [
                    {
                        backgroundColor: 'rgba(54, 162, 235, 0.8)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                    },
                    {
                        backgroundColor: 'rgb(247,86,86,0.8)',
                        borderColor: 'rgba(247,86,86, 1)',
                    },
                    {
                        backgroundColor: 'rgba(255, 206, 86, 0.8)',
                        borderColor: 'rgba(255, 206, 86, 1)',
                    }
                ];

                //Lưu các label vào 1 mảng
                centroidsData.data.centroids.forEach((cluster, key) => {
                    labels.push(`Cluster ${key}`);
                });

                //Lưu các giá trị các cluster vào 1 mảng
                centroidsData.data.centroids.forEach((cluster, key) => {
                    let isFirstIteration = true;
                    let item = Object.keys(cluster).map(key_item => {
                        //không lấy cột đầu tiên vì cột đầu là id(sẽ set null)
                        if (isFirstIteration) {
                            isFirstIteration = false;
                            return null;
                        } else {
                            if (key == 0) {
                                //Lặp 3 lần mà chỉ cần lấy 1 lần các label cho chục x thôi (nên p check lần lặp đàu tiên)
                                labels_column.push(key_item);
                            }
                            return cluster[key_item];
                        }
                    });

                    //Loại bỏ những phần tử nào = null
                    data.push(item.filter(value => value !== null));
                });


                //Xóa phần tử cuối cùng (Trong mongoDB có cột cluster)
                labels_column.pop()

                //Lưu các giá trị các dataset vào 1 mảng
                labels.forEach((label, key) => {
                    datasets.push({
                        label: label,
                        data: data[key],
                        backgroundColor: color_column[key].backgroundColor,
                        borderColor: color_column[key].borderColor,
                        borderWidth: 1
                    });
                })

                // Tạo dữ liệu mới cho biểu đồ
                const newChartData = {
                    labels: labels_column,
                    datasets: datasets
                };

                // Tạo biểu đồ mới
                newChart = new Chart(
                    document.getElementById('myChart'),
                    {
                        type: 'bar',
                        data: newChartData,
                    }
                );
                document.getElementsByClassName('chartCard')[0].classList.remove("d-none");;
                chartVisible = true;
            } else {
                console.log("Error: ", error);
            }
        } catch (error) {
            console.log("Error: ", error);
        }
    });
});
