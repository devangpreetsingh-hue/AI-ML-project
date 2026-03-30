import pandas as pd
from sklearn.linear_model import LinearRegression
import os

# Load data
file_path = "data.csv"
if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    data = pd.DataFrame({
        "RAM": [2,4,6,8,12,3,5,7,9,11],
        "Storage": [32,64,128,128,256,32,64,128,128,256],
        "Camera": [8,12,16,48,64,12,16,48,50,64],
        "Battery": [3000,4000,4500,5000,6000,3200,4200,4600,5200,6100],
        "Price": [7500,12000,15500,22000,32000,8000,13000,16000,23500,34000]
    })

# Features
X = data[["RAM","Storage","Camera","Battery"]]
y = data["Price"]

# model
model = LinearRegression()
model.fit(X, y)

# Applying recursive function
def get_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("that's not a number.Try again!")

# Loop for multiple phones
while True:
    print("\nLet's estimate your mobile's price!")

    ram = get_number("Enter RAM in GB: ")
    storage = get_number("Enter Storage in GB: ")
    camera = get_number("Enter Camera resolution in MP: ")
    battery = get_number("Enter Battery capacity in mAh: ")

    # PREDICTION
    predicted_price = model.predict([[ram, storage, camera, battery]])[0]
    print(f"\nEstimated Price: ₹{round(predicted_price)}")

    again = input("\nDo you want to try another phone? (y/n): ").strip().lower()
    if again != "y":
        print("\nThanks for using the mobile price predictor! Have a nice day ")
        break
