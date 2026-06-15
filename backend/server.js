const express = require("express");
const cors = require("cors");
require("dotenv").config();

const connectDB = require(
    "./config/db"
);

const churnRoute = require(
    "./routes/churnRoute"
);

const app = express();

connectDB();

app.use(
  cors({
    origin: "http://localhost:3000"
  })
);
app.use(express.json());

app.use(
    "/api/churn",
    churnRoute
);

const PORT = 8000;

app.listen(PORT, () => {

    console.log(
        `Server Running On ${PORT}`
    );
});