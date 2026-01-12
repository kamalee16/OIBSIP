import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "bmi_data.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Weight", "Height", "BMI", "Category", "Date"])


def calculate_bmi():
    try:
        name = entry_name.get().strip()
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be greater than zero")
            return

        # 🔹 Convert cm to meters if height looks like cm
        if height > 3:
            height = height / 100

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        save_data(name, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")



def save_data(name, weight, height, bmi, category):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            name, weight, height, round(bmi, 2),
            category, datetime.now().strftime("%Y-%m-%d")
        ])


def show_graph():
    name = entry_name.get()
    dates = []
    bmi_values = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"] == name:
                dates.append(row["Date"])
                bmi_values.append(float(row["BMI"]))

    if not bmi_values:
        messagebox.showinfo("No Data", "No data found for this user")
        return

    plt.plot(dates, bmi_values, marker='o')
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title(f"BMI Trend for {name}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("400x450")

tk.Label(root, text="Advanced BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (meters)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Button(root, text="Show BMI History Graph", command=show_graph).pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()