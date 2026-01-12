import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- Password Generator Logic ---------------- #
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return

    if length < 6:
        messagebox.showwarning("Weak Password", "Password length should be at least 6.")
    
    charset = ""
    
    if lower_var.get():
        charset += string.ascii_lowercase
    if upper_var.get():
        charset += string.ascii_uppercase
    if digit_var.get():
        charset += string.digits
    if symbol_var.get():
        charset += "!@#$%^&*()-_=+[]{};:,.<>/?"

    exclude_chars = exclude_entry.get()
    charset = ''.join(ch for ch in charset if ch not in exclude_chars)

    if not charset:
        messagebox.showerror("No Characters Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)

# ---------------- Password Strength Checker ---------------- #
def check_strength(password):
    strength = 0
    rules = [
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*()-_=+[]{};:,.<>/?" for c in password),
        len(password) >= 8
    ]
    
    strength = sum(rules)

    if strength <= 2:
        strength_label.config(text="Weak", fg="red")
    elif strength == 3:
        strength_label.config(text="Moderate", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

# ---------------- Clipboard Copy ---------------- #
def copy_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showinfo("Copy Failed", "No password to copy.")
    else:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("420x420")
root.resizable(False, False)

title = tk.Label(root, text="Advanced Password Generator", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Length
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

tk.Label(length_frame, text="Password Length: ").pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=5)
length_entry.insert(0, "12")
length_entry.pack(side=tk.LEFT)

# Checkboxes
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=digit_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack(anchor="w", padx=30)

# Exclude Characters
exclude_frame = tk.Frame(root)
exclude_frame.pack(pady=8)
tk.Label(exclude_frame, text="Exclude Characters: ").pack(side=tk.LEFT)
exclude_entry = tk.Entry(exclude_frame, width=20)
exclude_entry.pack(side=tk.LEFT)

# Generate Button
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, width=20, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Output
password_entry = tk.Entry(root, font=("Arial", 14), width=32, justify="center")
password_entry.pack(pady=5)

# Strength Label
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack()

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password, width=20, bg="#2196F3", fg="white")
copy_btn.pack(pady=10)

root.mainloop()
