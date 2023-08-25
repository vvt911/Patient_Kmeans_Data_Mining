const express = require("express");
const { getCentroidsNearest, getCentroids } = require("../controller/centroidController");

const centroidRouter = express.Router();

centroidRouter.post("/centroid-predict", getCentroidsNearest);
centroidRouter.get("/centroid-all", getCentroids);

module.exports = centroidRouter;