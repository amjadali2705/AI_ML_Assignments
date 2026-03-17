import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Simple Dataset (Square Footage vs Price)
data = {
    'sqft': [1500, 2000, 2500, 3000, 3500, 4000],
    'price': [300000, 400000, 500000, 600000, 700000, 800000]
}
df = pd.DataFrame(data)

# 2. Split Features and Target
X = df[['sqft']]
y = df['price']

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Training
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Testing
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f"Model MSE: {mse}")
print(f"Prediction for 2800 sqft: ${model.predict([[2800]])[0]:,.2f}")