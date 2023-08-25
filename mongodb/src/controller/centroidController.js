const { Centroids} = require('../model/centroidModel');
const { preprocessData } = require('../utils/dataUtils');
const { calculateDistance, getClusterFeatures } = require('../utils/centroidUtil');

// get all centroids and calculate the distance between each centroid and and patient in req.body
const getCentroidsNearest = async (req, res) => {
    try {
        const centroids = await Centroids.find().sort({ age: -1 });
        const centroidData = centroids.map(centroid => {
            return {
                age: centroid.age,
                chest_pain_type: centroid.chest_pain_type,
                blood_pressure: centroid.blood_pressure,
                cholesterol: centroid.cholesterol,
                max_heart_rate: centroid.max_heart_rate,
                exercise_angina: centroid.exercise_angina,
                plasma_glucose: centroid.plasma_glucose,
                insulin: centroid.insulin,
                bmi: centroid.bmi,
                hypertension: centroid.hypertension,
                heart_disease: centroid.heart_disease,
                smoking_status: centroid.smoking_status
            };
        });
        const patient = req.body;
        const patientProcessed = new Patients(await preprocessData(patient));

        let minDistance = Infinity;
        let centroidNearest = centroidData[0];
        for (let i = 0; i < centroidData.length; i++) {
            const centroid = centroidData[i];
            const distance = await calculateDistance(centroid, patientProcessed);
            if (minDistance > distance) {
                minDistance = distance;
                centroidNearest = centroid;
            }
        }
        
        const clusteredFetures = await getClusterFeatures(centroidNearest, centroidData);
        const result = await patientProcessed.save();

        res.status(200).json({
            status: 'success',
            data: {
                patient: result,
                centroid: centroidNearest,
                clusteredFetures: clusteredFetures,
            },
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message,
        });
    }
}; 

const getCentroids = async (req, res) => {
    try {
        const centroids = await Centroids.find();

        res.status(200).json({
            status: 'success',
            data: {
                centroids: centroids,
            },
        });
    } catch (error) {
        res.status(500).json({
            status: 'error',
            message: error.message,
        });
    }
};

module.exports = { getCentroidsNearest, getCentroids};