const express = require("express");
const axios = require("axios");

const Prediction = require(
    "../models/Prediction"
);

const router = express.Router();

router.post(
    "/predict",
    async (req, res) => {

        try {

            const response =
                await axios.post(
                    "http://127.0.0.1:5000/predict",
                    req.body
                );

            const result =
                response.data;

            // Save to MongoDB
            const newPrediction =
                new Prediction({

                    gender:
                        req.body.gender,

                    senior:
                        req.body.senior,

                    partner:
                        req.body.partner,

                    dependents:
                        req.body.dependents,

                    tenure:
                        req.body.tenure,

                    phone:
                        req.body.phone,

                    monthlyCharges:
                        req.body.monthlyCharges,

                    totalCharges:
                        req.body.totalCharges,

                    prediction:
                        result.prediction,

                    confidence:
                        result.confidence
                });

            await newPrediction.save();

            res.json({
                message:
                    "Prediction Saved",
                data: result
            });

        } catch (error) {

            console.log(
                error.message
            );

            res.status(500).json({
                error:
                    "Prediction Failed . Please Try Again."
            });
        }
    }
);

module.exports = router;
