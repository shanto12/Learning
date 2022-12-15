# Import necessary libraries
import numpy as np
import requests
from sklearn.linear_model import LinearRegression

# Load the data from coinmarket.com
url = 'https://au.investing.com/crypto/bitcoin/historical-data'
response = requests.get(url)

# Parse the data from the response
data = []
for line in response.text.split('\n'):
    if ',' in line:
        date, open_price, high, low, close_price, volume, market_cap = line.split(',')
        data.append([date, close_price])
data = np.array(data)
X = data[:, 0]  # Date
y = data[:, 1]  # Price

# Split the data into training and test sets
X_train = X[:int(X.shape[0]*0.8)]
y_train = y[:int(y.shape[0]*0.8)]
X_test = X[int(X.shape[0]*0.8):]
y_test = y[int(y.shape[0]*0.8):]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the price of Bitcoin
predictions = model.predict(X_test)

# Print the predictions
print(predictions)