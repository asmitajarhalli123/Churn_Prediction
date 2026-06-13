const mongoose = require("mongoose");

const predictionSchema = new mongoose.Schema({

    gender: {
        type:String
    },

    senior:{
        type:String
    },

    partner:{
        type:String
    },

    dependents:{
        type:String
    },

    tenure:{
        type:Number
    },

     phone: {
        type: String
    },

    monthlyCharges: {
        type: Number
    },

    totalCharges: {
        type: Number
    },

    prediction: {
        type: String
    },

    confidence: {
        type: Number
    },

    createdAt: {
        type: Date,
        default: Date.now
    }

});

module.exports = mongoose.model(
    "prediction" , predictionSchema
);