<div align="center">

# ⚡ Churn!Q
### *AI-Powered Telecom Customer Churn Prediction Platform*

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=28&duration=3000&color=00F7FF&center=true&vCenter=true&width=900&lines=Predict+Customer+Churn+Before+It+Happens;AI+Driven+Telecom+Analytics;Powered+By+MERN+%2B+TensorFlow%2FKeras;Real-Time+Churn+Prediction+Engine" />

---

![MERN](https://img.shields.io/badge/MERN-Stack-00ED64?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge&logo=mongodb)
![React](https://img.shields.io/badge/React.js-Frontend-61DAFB?style=for-the-badge&logo=react)
![NodeJS](https://img.shields.io/badge/Node.js-Backend-339933?style=for-the-badge&logo=node.js)
![Express](https://img.shields.io/badge/Express.js-API-000000?style=for-the-badge&logo=express)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow)
![ANN](https://img.shields.io/badge/AI-Artificial%20Neural%20Network-FF007A?style=for-the-badge)

### 🧠 *Predict Churn. Retain Customers. Maximize Revenue.*

</div>

---

# 🌌 About Churn!Q

**Churn!Q** is an advanced **AI-powered Telecom Customer Churn Prediction Platform** engineered to proactively identify customers who are likely to discontinue telecom services.

Built using the **MERN Stack** and powered by an **Artificial Neural Network (ANN)** developed with **TensorFlow/Keras**, the platform transforms customer behavioral and subscription data into actionable churn intelligence.

Instead of reacting after customer loss, **Churn!Q enables telecom businesses to predict churn before it occurs**, empowering retention teams with intelligent insights and confidence-driven recommendations.

---

# ⚡ Why Churn!Q?

Customer churn directly impacts telecom profitability.

Traditional analytics struggle to detect hidden behavioral patterns responsible for customer attrition.

**Churn!Q solves this challenge using Neural Network intelligence**, enabling:

✅ Early churn detection  
✅ Revenue protection  
✅ Smarter retention strategies  
✅ AI-powered customer risk scoring  
✅ Real-time churn confidence analysis

---

# 🧠 AI Intelligence Behind Churn!Q

At the core of **Churn!Q** lies an **Artificial Neural Network (ANN)** model trained using **TensorFlow/Keras**.

The neural network analyzes telecom customer attributes and predicts churn probability using hidden pattern recognition.

### Input Features Used

```javascript
{
  gender: "",
  senior: "",
  partner: "",
  dependents: "",
  tenure: "",
  phone: "",
  monthlyCharges: "",
  totalCharges: ""
}
```

### Prediction Output

The model predicts:

- **Customer Churn Risk**
- **Retention Probability**
- **AI Confidence Score**
- **Risk Classification**

Example:

```yaml
Prediction: HIGH CHURN RISK
Confidence Score: 94.6%
Status: Immediate Retention Recommended
```

---

# 🚀 Key Features

## 🔥 Real-Time Churn Prediction
Get **instant telecom churn predictions** powered by Neural Networks.

## 🧠 AI Confidence Score
Each prediction is accompanied by an **AI confidence score** for better decision-making accuracy.

## 📊 Futuristic Dashboard
A visually immersive dashboard designed for intuitive telecom analytics.

## ⚡ Intelligent Prediction Panel
Simple form-based prediction system for real-time customer churn assessment.

## 🔄 REST API Integration
Robust backend API architecture for prediction handling.

## 📱 Responsive Interface
Optimized for desktop, tablet, and mobile experiences.

---

# 🏗️ System Architecture

```text
                ┌────────────────────┐
                │   React Frontend   │
                │  Dashboard + Form  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Express REST APIs  │
                │ localhost:8000     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ TensorFlow/Keras   │
                │ ANN Prediction     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     MongoDB        │
                │ Customer Dataset   │
                └────────────────────┘
```

---

# 🛠️ Tech Stack

## Frontend

- **React.js**
- Modern UI Components
- Responsive Design
- Dynamic Form Handling

## Backend

- **Node.js**
- **Express.js**
- RESTful API Architecture

## AI/ML

- **TensorFlow**
- **Keras**
- Artificial Neural Network (ANN)

## Database

- **MongoDB**

---

# 📂 Project Structure

```bash
ChurnQ/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── App.js
│
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── server.js
│   └── api/
│
├── model/
│   ├── churn_model.h5
│   ├── preprocessing.py
│   └── prediction_engine.py
│
├── database/
│
└── README.md
```

---

# 🌐 REST API Endpoint

### Churn Prediction API

```http
POST http://localhost:8000/api/churn
```

### Request Body

```json
{
  "gender": "Female",
  "senior": 1,
  "partner": "Yes",
  "dependents": "No",
  "tenure": 12,
  "phone": "Yes",
  "monthlyCharges": 85.5,
  "totalCharges": 1050
}
```

### Response Example

```json
{
  "prediction": "High Churn Risk",
  "confidenceScore": "94.6%",
  "status": "Retention Required"
}
```

---



---

# 🖥️ Dashboard Preview

### 🚀 Prediction Panel

- Enter telecom customer information
- Run AI-powered prediction
- View confidence score instantly

### 📊 Analytics Dashboard

- Churn statistics
- Customer insights
- Retention indicators
- Prediction summaries

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/yourusername/ChurnQ.git
```

---

## Install Frontend Dependencies

```bash
cd frontend
npm install
npm start
```

---

## Install Backend Dependencies

```bash
cd backend
npm install
node server.js
```

---

## Run Backend Server

```bash
localhost:8000
```

---


# Screenshots (Dashboard)

<img width="1872" height="892" alt="image" src="https://github.com/user-attachments/assets/7656e120-e532-4453-a674-c445c2e4bfff" />

<img width="1890" height="887" alt="image" src="https://github.com/user-attachments/assets/3f593c35-3e1e-46f7-9270-170803103edc" />

<img width="1871" height="892" alt="image" src="https://github.com/user-attachments/assets/b895dd6b-f8d5-4c51-89f9-5efe539eac62" />

<img width="1880" height="892" alt="image" src="https://github.com/user-attachments/assets/230a5cb1-c8ca-4ddf-8421-29875edd687d" />





# 🔮 Future Enhancements

- 📈 Advanced churn analytics
- 🤖 Explainable AI predictions
- ☁️ Cloud deployment
- 📊 Interactive data visualization
- 🔔 Automated retention alerts
- 🧠 Deep Learning optimization
- 📥 CSV bulk prediction upload

---

# 💡 What Makes Churn!Q Unique?

Unlike traditional churn systems that rely purely on statistical assumptions, **Churn!Q leverages Neural Intelligence to uncover hidden churn signals** that conventional analytics often fail to detect.

Its combination of:

### ⚡ MERN Ecosystem  
### 🧠 ANN Intelligence  
### 📊 Confidence-Based Predictions  
### 🚀 Real-Time API Processing

creates a scalable and intelligent churn prediction environment.

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve **Churn!Q**, feel free to:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to branch
5. Open a Pull Request

---

# 👩‍💻 Author

## **@smita**

### Building intelligent systems with AI & Full Stack Engineering 🚀

---

<div align="center">

### ⭐ If you found this project useful, don't forget to star the repository!

**Built with ❤️ using MERN + TensorFlow/Keras**

</div>
