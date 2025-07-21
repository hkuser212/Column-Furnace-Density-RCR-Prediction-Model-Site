# 🔥 Column-Furnace-Density-RCR-Prediction-Model-Site

📊 **Predicting Product Densities & RCR using Machine Learning for Refinery Optimization**

---

## 📁 Project Summary

This project was developed as part of my internship at **Indian Oil Corporation Limited (IOCL) – Guwahati Refinery**, under the supervision of senior chemical engineers and data science mentors. The goal was to predict key product output properties from the **Column Furnace unit**, a critical component in the refinery's product distillation system.

We built a **full-stack ML solution** that predicts **densities of multiple fractions** and **Ramsbottom Carbon Residue (RCR)** using historical refinery process data.

---

## 🎯 Problem Statement

Refineries often rely on lab-based testing for product quality parameters such as:

- **CFO Density** (Clarified Fuel Oil)
- **CKO Density** (Cracked Kerosene Oil)
- **CGO Density** (Cracked Gas Oil)
- **CGO RCR** (Carbon Residue)

However, these test results take time and cannot be used for real-time decision-making. The aim of this project was to:

- Predict these parameters in advance  
- Reduce dependency on lab results  
- Assist engineers in adjusting furnace conditions in real time  

---

## 🛠️ Tech Stack

- **Machine Learning**: `XGBoost`, `MultiOutputRegressor`, `Optuna`  
- **Data Processing**: `Pandas`, `NumPy`, `Scikit-learn`  
- **Dashboard Interface**: `Streamlit`, `Django`, `Chart.js`  
- **Visualization**: `Matplotlib`, `Seaborn`  
- **Deployment**: Localhost (optionally extendable to refinery intranet)  

---

## 📌 Features

### ✅ Multi-Output ML Model
- Trained on historical operational and lab data  
- Predicts **all four target parameters** simultaneously  
- Hyperparameters optimized with **Optuna**  

### ✅ Autofill Input Values
- Autofills suggestions from recent historical rows  
- Helps engineers pre-populate inputs with known-good values  

### ✅ Visualization Dashboard
- Bar charts comparing **actual vs predicted values**  
- Feature importance charts for each target  
- Error analysis and **R² scores** for model evaluation  

### ✅ Profit Impact & Alerts (Planned Scope)
- Threshold-based alerts for values outside safe ranges  
- Cost impact estimation based on quality deviation  

---

## 📈 Results

| Target Parameter | R² Score (Test Data) |
|------------------|----------------------|
| CFO Density      | ~0.72                |
| CKO Density      | ~0.70                |
| CGO Density      | ~0.68                |
| CGO RCR          | ~0.81                |

- **Total RMSE**: ~5.03  
- **MAE**: ~3.31  
- Cross-validated using `TimeSeriesSplit`

---

## 👨‍🔬 Industrial Relevance

- Built using **real refinery data** provided by IOCL  
- Validated by **chemical engineering logic and domain constraints**  
- Received feedback from **process engineers** to tune model behavior  

---



## 📌 Future Scope

- Integration with **live furnace monitoring systems** via APIs  
- Deployment to refinery intranet as a **secure, role-based web app**  
- Incorporation of **confidence intervals** and **SHAP-based model explainability**  

---

## 📥 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ColumnFurnace-ML.git
cd ColumnFurnace-ML

```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt

```

### 3️⃣ Run the application
```bash
python manage.py runserver  # For local development
python manage.py runserver 0.0.0.0:8000  # For deployment

```
🔗 Code Base - https://github.com/hkuser212/Column-Furnace-Density-RCR-Prediction-Model

🔗 DCU Furnace – SAD Prediction Project (ML dashboard for predicting shutdown timing)

---

Let's Connect!

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hkuser212)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsh210204/)

Screenshots of the dashboard are available in the [**Readme**](https://github.com/hkuser212/Column-Furnace-Density-RCR-Prediction-Model) of this repository.


