import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("house_data.csv")

print(df.head())
X = df[["Size", "Rooms"]]
y = df["Price"]
model = LinearRegression()

model.fit(X, y)
new_house = pd.DataFrame([[130, 3]], columns=["Size", "Rooms"])
prediction = model.predict(new_house)

prediction = model.predict(new_house)

print("Predicted Price:", prediction)