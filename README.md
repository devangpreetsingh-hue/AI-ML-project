# 📱 Mobile Price Prediction System

## 📖 Introduction
This project is developed as part of academic coursework to demonstrate the application of machine learning in predicting mobile phone prices. The system estimates the price of a smartphone based on its specifications such as RAM, Storage, Camera, and Battery capacity.

## 🎯 Objective
The main objectives of this project are:
- To understand the basics of Machine Learning
- To implement a Linear Regression model
- To predict mobile prices using given features
- To build a simple command-line based application

## 🛠️ Technologies Used
- Python 3
- pandas library
- scikit-learn library

## 📊 Dataset Description
The dataset used in this project contains the following features:
- RAM (in GB)
- Storage (in GB)
- Camera (in MP)
- Battery (in mAh)
- Price (in INR)

Note: If an external dataset file (data.csv) is not available, the program uses a predefined dataset within the code.

## ⚙️ Methodology
1. Data is loaded using pandas  
2. Features (RAM, Storage, Camera, Battery) are separated as input variables  
3. Price is taken as the target variable  
4. A Linear Regression model is trained using the dataset  
5. User inputs are taken through the command line  
6. The trained model predicts the estimated price  

## ▶️ How to Run the Project

### Install required libraries:
pip install pandas scikit-learn

### Run the Python file:
python main.py

### Enter the required mobile specifications when prompted.

## 💡 Sample Output

Let's estimate your mobile's price!

Enter RAM in GB: 8  
Enter Storage in GB: 128  
Enter Camera resolution in MP: 48  
Enter Battery capacity in mAh: 5000  

Estimated Price: ₹22000

## ✅ Features
- Simple and easy to use  
- Accepts user input dynamically  
- Provides instant price prediction  
- Works even without external dataset file  

## ⚠️ Limitations
- Small dataset may reduce accuracy  
- Only Linear Regression is used  
- Does not consider brand or processor details  

## 🔮 Future Scope
- Use larger and real-world datasets  
- Implement advanced machine learning models  
- Develop a graphical or web-based interface  
- Include more features like brand and processor  

## 👨‍🎓 Conclusion
This project demonstrates how machine learning can be applied to solve real-world problems like price prediction. It also helps in understanding data processing, model training, and user interaction in Python.

## 👤 Author
Name: Devangpreet Singh  
Registration Number: 25BCE10565
