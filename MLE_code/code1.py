import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

df = pd.read_csv("housing_price_prediction.csv")


# --------------------------------------------------
# 2. Inspect the dataset
# --------------------------------------------------

print(df.head(5))
print("\n")

print(df.shape)
print("\n")

print(df.max(numeric_only=True))
print("\n")


# --------------------------------------------------
# 3. Separate features and target
# --------------------------------------------------

y = df["SalePrice"]

X = df.drop("SalePrice", axis=1)


# --------------------------------------------------
# 4. Select numerical columns
# --------------------------------------------------

X_numerical = X.select_dtypes(include=np.number)


# Fill missing values with column mean

X_numerical = X_numerical.fillna(X_numerical.mean())


# --------------------------------------------------
# 5. Split the data
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_numerical,
    y,
    test_size=0.3,
    random_state=50
)


# --------------------------------------------------
# 6. Create and train Linear Regression model
# --------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)


# --------------------------------------------------
# 7. Evaluate the model
# --------------------------------------------------

train_score = model.score(X_train, y_train)

test_score = model.score(X_test, y_test)

print(f"Training R^2 score: {train_score:.4f}")
print(f"Test R^2 score: {test_score:.4f}")

print("\nFirst 5 rows of X_train after preprocessing:\n")

print(X_train.head())


# --------------------------------------------------
# 8. Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 9. Plot Actual vs Predicted values
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    x=y_test,
    y=y_pred
)

plt.xlabel("Actual SalePrice")
plt.ylabel("Predicted SalePrice")

plt.title("Actual vs. Predicted SalePrice")


# Diagonal reference line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.grid(True)

plt.show()

import matplotlib.pyplot as plt

plt.boxplot(df["SalePrice"])

plt.ylabel("Sale Price")
plt.title("Sale Price Box Plot")

plt.show()