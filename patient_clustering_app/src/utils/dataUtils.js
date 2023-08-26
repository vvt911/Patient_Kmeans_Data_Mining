
const minMaxScaling = (value, min, max) => {
    return (value - min) / (max - min);
};

const preprocessData = async (data) => {
    const ranges = {
        age: { min: 28, max: 82 },
        blood_pressure: { min: 90, max: 165 },
        cholesterol: { min: 150, max: 294 },
        max_heart_rate: { min: 138, max: 202 },
        plasma_glucose: { min: 55, max: 199 },
        insulin: { min: 81, max: 171 },
        bmi: { min: 10.3, max: 66.8 },
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
        preprocessedData.smoking_status = 2;
    } else if (preprocessedData.smoking_status === "never smoked") {
        preprocessedData.smoking_status = 0;
    } else if (preprocessedData.smoking_status === "formerly smoked") {
        preprocessedData.smoking_status = 1;
    }   else if (preprocessedData.smoking_status === "smokes") {
        preprocessedData.smoking_status = 3;
    }

    return preprocessedData;
};

module.exports = { preprocessData };