const express = require("express");
const cors = require("cors");

const churnRoute = require("./routes/churnRoute");

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/churn", churnRoute);

const PORT = 8000;

app.listen(PORT, () => {
  console.log(`Server Running On ${PORT}`);
});