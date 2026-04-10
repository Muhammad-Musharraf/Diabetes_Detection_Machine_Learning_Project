# 🩺 Diabetes Detection using Machine Learning

An end-to-end **Machine Learning project** that predicts whether a person is diabetic or not based on medical attributes such as glucose level, blood pressure, BMI, insulin, and more.

This project demonstrates the complete ML pipeline including **data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using a web application**.

---

## 🚀 Live Demo

👉 **Try the App Here:**
🔗 https://diabetesdetectionmachinelearningproject.streamlit.app/

---

## 🚀 Project Overview

Diabetes is a chronic disease that affects millions of people worldwide. Early detection plays a crucial role in preventing severe complications. This project leverages **machine learning algorithms** to build a predictive system for diabetes diagnosis.

The model is trained on a structured dataset containing medical features and outputs a **binary classification (Diabetic / Non-Diabetic)**.

---

## 📊 Dataset

The dataset used in this project includes the following features:

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI (Body Mass Index)
* Diabetes Pedigree Function
* Age
* Outcome (Target Variable)

> The dataset is commonly based on the **Pima Indians Diabetes Dataset**, widely used for ML classification tasks ([GitHub][1])

---

## ⚙️ Tech Stack

* **Programming Language:** Python
* **Libraries:**

  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib / Seaborn
* **Modeling:** Machine Learning Algorithms
* **Deployment:** Streamlit

---

## 🔍 Project Workflow

1. **Data Collection**
2. **Data Preprocessing**

   * Handling missing values
   * Feature scaling
3. **Exploratory Data Analysis (EDA)**
4. **Feature Selection**
5. **Model Training**

   * Logistic Regression
   * Decision Tree / Random Forest
6. **Model Evaluation**

   * Accuracy Score
   * Confusion Matrix
7. **Model Saving**
8. **Web App Deployment**

---

## 🤖 Machine Learning Models

* Logistic Regression
* Naive Bayes
* Random Forest
* Support Vector Machine

These models are trained and evaluated to select the best-performing model.

---

## 📈 Results

* Achieved high accuracy on test data
* Model successfully predicts diabetes risk based on input features
* Can be used as a **basic healthcare decision support system**

---

## 🖥️ Web Application

A simple and interactive **Streamlit web app** is built where users can:

* Input medical parameters
* Get instant prediction result
* User-friendly interface for real-world usage

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Muhammad-Musharraf/Diabetes_Detection_Machine_Learning_Project.git
cd Diabetes_Detection_Machine_Learning_Project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── diabetes (2).csv           # Dataset files
├── diabetes_detection.ipnb    # Jupyter notebooks (EDA & training)
├── pipe.plk                   # Saved model (pickle file)
├── App.py                     # Web application
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation        
```

---

## 🎯 Key Features

✔ End-to-End ML Pipeline
✔ Clean and Structured Code
✔ Model Deployment
✔ Real-world Healthcare Use Case
✔ Beginner-Friendly Project

---

## 📌 Future Improvements

* Improve model accuracy using advanced algorithms
* Add deep learning models
* Deploy on cloud (AWS / Render / Streamlit Cloud)
* Add more medical features for better prediction

---

## 👨‍💻 Author

**Muhammad Musharraf**

* GitHub: [https://github.com/Muhammad-Musharraf](https://github.com/Muhammad-Musharraf)

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share with others

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

### 🔥 Tip (Important)

If you haven’t deployed yet, you can deploy easily on:

* [https://streamlit.io/cloud](https://streamlit.io/cloud)

