import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load dataset
df = pd.read_csv("data/house_prices.csv")

print("--- 1. Data Exploration ---")
print("First 5 rows of the dataset:")
print(df.head())
print("\n" + "=" * 50 + "\n")

print("Information about the dataset:")
df.info()
print("\n" + "=" * 50 + "\n")

print("Statistical summary of the dataset:")
print(df.describe())
print("\n" + "=" * 50 + "\n")

# 2. Data preprocessing
# Address is text, so it is not used as a model feature.
X = df[
    [
        "Avg_Area_Income",
        "Avg_Area_House_Age",
        "Avg_Area_Number_of_Rooms",
        "Avg_Area_Number_of_Bedrooms",
        "Area_Population",
    ]
]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=101
)

# 3. Train Linear Regression model
print("--- 2. Training the Model ---")
lm = LinearRegression()
lm.fit(X_train, y_train)

print("Linear Regression model has been trained.")
print("\n" + "=" * 50 + "\n")

# 4. Model evaluation
print("--- 3. Evaluating the Model ---")

coeff_df = pd.DataFrame(lm.coef_, X.columns, columns=["Coefficient"])
print("Model Coefficients:")
print(coeff_df)
print()

predictions = lm.predict(X_test)

mae = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("\n" + "=" * 50 + "\n")

# 5. Visualize results
print("--- 4. Visualizing Predictions ---")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, edgecolors="black", alpha=0.7)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.plot(
    [min(y_test), max(y_test)],
    [min(y_test), max(y_test)],
    color="red",
    linestyle="--",
    lw=2,
)
plt.grid(True)
plt.tight_layout()
plt.show()

residuals = y_test - predictions

sns.displot(residuals, bins=20, kde=True)
plt.title("Distribution of Residuals")
plt.xlabel("Residuals (Actual - Predicted)")
plt.tight_layout()
plt.show()

print("\n--- Project Complete ---")
print("The scatter plot compares actual and predicted house prices.")
print("The residual distribution shows the prediction errors.")
