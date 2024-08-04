import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Reading data from Excel file
file_path = 'PowerBI_Data.xlsx'
data = pd.read_excel(file_path)

# Converting the date column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Extracting time features from the date column
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day

# Dropping the original date column and TransactionID column
data = data.drop(['Date', 'TransactionID'], axis=1)

# Displaying the preprocessed data
print(data.head())

# Splitting the data into independent variables (X) and dependent variable (y)
X = data.drop('TotalAmount', axis=1)
y = data['TotalAmount']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Building a linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test_scaled)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Showing a few samples of actual vs predicted values
comparison = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print(comparison.head(10))
