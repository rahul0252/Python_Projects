import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = "users_data.json"

# Function to load user data from a JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save user data to a JSON file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return None

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to submit data (calculate BMI and save data)
def submit_data(username, weight, height):
    bmi = calculate_bmi(weight, height)
    if bmi is None:
        messagebox.showerror("Error", "Height cannot be zero.")
        return

    category = categorize_bmi(bmi)
    result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    
    user_data = data.get(username, [])
    user_data.append({"date": str(datetime.now()), "bmi": bmi})
    data[username] = user_data
    save_data(data)

# Function to visualize user data (BMI trends over time)
def visualize_data(username):
    user_data = data.get(username, [])
    if not user_data:
        messagebox.showinfo("No Data", "No data available for this user.")
        return
    
    dates = [record["date"] for record in user_data]
    bmis = [record["bmi"] for record in user_data]
    
    plt.plot(dates, bmis, marker='o')
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title(f"BMI Trend for {username}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to handle the submission of data (with input validation)
def on_submit():
    username = username_entry.get().strip()
    try:
        weight = float(weight_entry.get().strip())
        height = float(height_entry.get().strip()) / 3.281  # Convert height from feet to meters
        if weight <= 0 or height <= 0:
            raise ValueError("Invalid input")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
        return

    submit_data(username, weight, height)

# Function to handle the visualization of data
def on_visualize():
    username = username_entry.get().strip()
    visualize_data(username)

# GUI Setup
app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(app)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
weight_entry = tk.Entry(app)
weight_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Height (feet):").grid(row=2, column=0, padx=10, pady=5)
height_entry = tk.Entry(app)
height_entry.grid(row=2, column=1, padx=10, pady=5)

result_label = tk.Label(app, text="Your BMI will appear here", font=("Arial", 12))
result_label.grid(row=3, columnspan=2, padx=10, pady=10)

submit_button = tk.Button(app, text="Calculate BMI", command=on_submit)
submit_button.grid(row=4, column=0, padx=10, pady=10)

visualize_button = tk.Button(app, text="Visualize Data", command=on_visualize)
visualize_button.grid(row=4, column=1, padx=10, pady=10)

# Load data
data = load_data()

# Run the app
app.mainloop()
