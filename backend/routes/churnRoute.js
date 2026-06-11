const express = require("express");
const axios = require("axios");

const router = express.Router();

router.post("/predict", async (req, res) => {

    try {

        const response = await axios.post(
            "http://127.0.0.1:5000/predict",
            req.body
        );

        res.json(response.data);

    } catch (error) {

        console.log("FULL ERROR:");
        console.log(error.message);

        if (error.response) {
            console.log(error.response.data);
        }

        res.status(500).json({
            error: "Prediction Failed",
            details: error.message
        });
    }
});

module.exports = router;