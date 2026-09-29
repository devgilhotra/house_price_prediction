# 🏠 House Price Prediction

A beginner-friendly **Machine Learning project** that predicts house prices using **Linear Regression** with Python and scikit-learn.

## 📌 Project Overview

This project demonstrates a complete basic machine learning workflow:

- Loading a CSV dataset
- Exploring the dataset with Pandas
- Selecting features and target variables
- Splitting data into training and testing sets
- Training a Linear Regression model
- Generating predictions
- Evaluating the model using MAE, MSE, and RMSE
- Visualizing actual vs. predicted prices
- Visualizing the distribution of residuals

## 🧠 Machine Learning Algorithm

**Linear Regression**

The model uses the following numerical features to predict `Price`:

- Average Area Income
- Average Area House Age
- Average Area Number of Rooms
- Average Area Number of Bedrooms
- Area Population

The `Address` column is retained in the dataset but is not used as a model feature because it is text data.

## 📂 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── house_prices.csv
│
├── house_price_prediction.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset

The project uses a small sample house-price dataset included in this repository.

### Dataset columns

| Column | Description |
|---|---|
| `Avg_Area_Income` | Average income in the area |
| `Avg_Area_House_Age` | Average age of houses in the area |
| `Avg_Area_Number_of_Rooms` | Average number of rooms |
| `Avg_Area_Number_of_Bedrooms` | Average number of bedrooms |
| `Area_Population` | Population of the area |
| `Price` | House price / target variable |
| `Address` | House address |

> **Note:** This repository contains a small sample dataset for learning and demonstration. It should not be treated as a production-grade real-estate dataset.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd house-price-prediction
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

From the project root directory:

```bash
python house_price_prediction.py
```

The program will:

1. Load the dataset.
2. Display the first rows.
3. Display dataset information.
4. Display descriptive statistics.
5. Split the dataset into training and testing sets.
6. Train a Linear Regression model.
7. Display model coefficients.
8. Calculate MAE, MSE, and RMSE.
9. Display prediction and residual visualizations.

## 📈 Model Evaluation

The project calculates:

### Mean Absolute Error (MAE)

Measures the average absolute difference between actual and predicted prices.

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted prices.

### Root Mean Squared Error (RMSE)

The square root of MSE, expressed in the same units as the target variable.

## 📊 Visualizations

The project generates two visualizations:

1. **Actual Prices vs. Predicted Prices**  
   Compares the model's predictions with the actual test-set prices.

2. **Distribution of Residuals**  
   Shows the distribution of prediction errors.

## 🔍 Machine Learning Workflow

```text
Dataset
   ↓
Data Exploration
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Predictions
   ↓
Model Evaluation
   ↓
Visualization
```

## 🎯 Learning Objectives

This project is useful for practicing:

- Python for Machine Learning
- Pandas data handling
- NumPy calculations
- Exploratory data analysis
- Train/test splitting
- Linear Regression
- Model coefficients
- Regression evaluation metrics
- Data visualization
- Residual analysis

## 🚀 Possible Future Improvements

For a larger and more realistic version of this project, the following could be added:

- A larger real-world dataset
- Data cleaning and missing-value handling
- Outlier detection
- Feature scaling where appropriate
- Additional regression algorithms
- Cross-validation
- Hyperparameter tuning
- Model comparison
- Feature importance / coefficient analysis
- A Streamlit prediction interface

## 👨‍💻 Author

**Dev Gilhotra**

GitHub: Add your GitHub profile link here  
LinkedIn: Add your LinkedIn profile link here  
Portfolio: Add your portfolio link here

---

⭐ If you found this project useful for learning Machine Learning, consider starring the repository.
