const { Centroids} = require('../model/centroidModel');
const { Patients } = require('../model/patientModel');
const { preprocessData } = require('../utils/dataUtils');
const { calculateDistance, getClusterFeatures } = require('../utils/centroidUtil');

const getCentroidsNearest = async (req, res) => {
    try {
        const centroids = await Centroids.find();
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
                smoking_status: centroid.smoking_status,
                cluster: centroid.cluster
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
        
        const clusteredFeatures = await getClusterFeatures(centroidNearest);
        const result = await patientProcessed.save();

        res.status(200).json({
            status: 'success',
            data: {
                patient: result,
                centroid: centroidNearest,
                clusteredFeatures: clusteredFeatures,
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