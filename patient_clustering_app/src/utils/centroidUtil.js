// calculate the distance between two points
const calculateDistance = async (point1, point2) => {
    const distance = Math.sqrt(
        Math.pow(point1.age - point2.age, 2) +
        Math.pow(point1.chest_pain_type - point2.chest_pain_type, 2) +
        Math.pow(point1.blood_pressure - point2.blood_pressure, 2) +
        Math.pow(point1.cholesterol - point2.cholesterol, 2) +
        Math.pow(point1.max_heart_rate - point2.max_heart_rate, 2) +
        Math.pow(point1.exercise_angina - point2.exercise_angina, 2) +
        Math.pow(point1.plasma_glucose - point2.plasma_glucose, 2) +
        Math.pow(point1.insulin - point2.insulin, 2) +
        Math.pow(point1.bmi - point2.bmi, 2) +
        Math.pow(point1.hypertension - point2.hypertension, 2) +
        Math.pow(point1.heart_disease - point2.heart_disease, 2) +
        Math.pow(point1.smoking_status - point2.smoking_status, 2)
    );
    return distance;
};

const getClusterFeatures = async (centroid, centroidData) => {
    if (centroid.cluster == 0) {
        return {
            name: "Cluster 0",
            features: "Bệnh nhân có sức khỏe ổn định",
            color_text: "text-success"
        };
    } else if (centroid.cluster == 1) {
        return {
            name: "Cluster 1",
            features: "Bệnh nhân có nguy cơ rất lớn mắc các bệnh về tim mạch",
            color_text: "text-danger"
        };
    } else if (centroid.cluster == 2) {
        return {
            name: "Cluster 2",
            features: "Bệnh nhân có nguy cơ mắc các bệnh về tim mạch",
            color_text: "text-warning"
        };
    }
};


module.exports = { calculateDistance , getClusterFeatures};