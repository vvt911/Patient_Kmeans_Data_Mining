
const minMaxScaling = (value, min, max) => {
    return (value - min) / (max - min);
};

const preprocessData = async (data) => {
    const ranges = {
        age: { min: 28, max: 82 },
        blood_pressure: { min: 90, max: 180 },
        cholesterol: { min: 120, max: 300 },
        max_heart_rate: { min: 70, max: 220 },
        plasma_glucose: { min: 70, max: 250 },
        insulin: { min: 82, max: 180 },
        bmi: { min: 10, max: 50 },
    };

    const preprocessedData = { ...data };

    for (const attribute in ranges) {
        if (preprocessedData.hasOwnProperty(attribute)) {
            preprocessedData[attribute] = minMaxScaling(
                preprocessedData[attribute],
                ranges[attribute].min,
                ranges[attribute].max
            );
        }
    }

    if (preprocessedData.smoking_status === "Unknown") {
        preprocessedData.smoking_status = 0;
    } else if (preprocessedData.smoking_status === "never smoked") {
        preprocessedData.smoking_status = 2;
    } else if (preprocessedData.smoking_status === "formerly smoked") {
        preprocessedData.smoking_status = 1;
    }   else if (preprocessedData.smoking_status === "smokes") {
        preprocessedData.smoking_status = 3;
    }

    return preprocessedData;
};

module.exports = { preprocessData };