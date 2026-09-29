# 📱 Mobile Price Predictor

A Machine Learning web application that predicts the estimated price of a smartphone based on its specifications using **Linear Regression** and **Streamlit**.

## 📌 Project Description

The Mobile Price Predictor accepts smartphone specifications such as RAM, storage, battery capacity, screen size, camera resolution, and processor score.

A Linear Regression model is trained using the available dataset and predicts the estimated price of a new smartphone.

The complete application is developed using Python and Streamlit.

---

## 🎯 Objectives

* Predict mobile phone prices using Machine Learning.
* Implement Linear Regression.
* Analyze mobile specifications and their relationship with price.
* Build an interactive Streamlit application.
* Evaluate the model using MSE and R² Score.
* Visualize the dataset using graphs and a correlation heatmap.

---

## 🧠 Machine Learning Algorithm

### Linear Regression

Linear Regression is a supervised Machine Learning algorithm used to predict continuous numerical values.

### Input Features

```text
RAM
Storage
Battery
Screen Size
Camera
Processor Score
```

### Target Variable

```text
Price
```

The model learns the relationship between the input features and mobile price.

---

## 📊 Dataset

The dataset contains the following columns:

| Column         | Description                 |
| -------------- | --------------------------- |
| RAM            | RAM capacity in GB          |
| Storage        | Internal storage in GB      |
| Battery        | Battery capacity in mAh     |
| ScreenSize     | Screen size in inches       |
| Camera         | Camera resolution in MP     |
| ProcessorScore | Processor performance score |
| Price          | Mobile price in INR         |

---

## 🏗️ Project Structure

```text
Mobile_Price_Predictor/
│
├── data/
│   └── mobile_prices.csv
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## 🔄 Project Workflow

```text
Mobile Dataset
      ↓
Load Dataset
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Linear Regression
      ↓
Model Training
      ↓
Prediction
      ↓
Model Evaluation
      ↓
Streamlit Dashboard
```

---

## 📈 Model Evaluation

### Mean Squared Error (MSE)

MSE measures the average squared difference between the actual and predicted prices.

A lower MSE generally indicates smaller prediction errors.

### R² Score

R² Score measures how much of the variation in mobile prices is explained by the model.

A value closer to 1 generally indicates that the model explains more of the variation in the target variable.

---

## 🖥️ Application Features

### 🔮 Price Prediction

The user can enter:

* RAM
* Storage
* Battery
* Screen Size
* Camera
* Processor Score

The application then predicts the estimated mobile price.

### 📊 Dataset View

The complete dataset can be viewed inside the Streamlit application.

### 📈 Price Statistics

The application displays:

* Average Price
* Minimum Price
* Maximum Price

### 📉 Data Visualization

The user can select different features and view their relationship with mobile price.

### 🔥 Correlation Heatmap

A correlation heatmap is provided to understand relationships between numerical variables.

### 🤖 Model Information

The application displays:

* MSE
* R² Score
* Linear Regression coefficients
* Intercept

---

## ⚙️ Installation

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install the required libraries

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 📝 Example Input

```tex
```
