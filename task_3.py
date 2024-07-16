import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    result_var.set("Generated Password: " + password)

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Enter password length:").pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=10)

root.mainloop()
