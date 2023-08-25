const express = require("express");
const { getCentroidsNearest } = require("../controller/centroidController");

const centroidRouter = express.Router();

centroidRouter.post("/centroid-predict", getCentroidsNearest);

module.exports = centroidRouter;