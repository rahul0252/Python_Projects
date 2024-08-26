import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid positive integer for the password length.")
        return

    use_upper = var_upper.get()
    use_lower = var_lower.get()
    use_numbers = var_numbers.get()
    use_symbols = var_symbols.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Input Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(0, tk.END)
    password_display.insert(0, password)
    password_display.config(state='readonly')

def copy_to_clipboard():
    password = password_display.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No password to copy. Please generate one first.")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x450")
root.resizable(True, True)

# Set window transparency
root.attributes('-alpha', 0.9)  # Adjust the alpha value between 0 (fully transparent) and 1 (fully opaque)

# Background Color (Solid Color)
style_bg = '#333333'  # Dark gray background (change as needed)
frame = tk.Frame(root, bg=style_bg)
frame.pack(fill='both', expand=True, padx=20, pady=20)

# Password Length
length_label = tk.Label(frame, text="Enter the Password Length:", bg=style_bg, font=('Arial', 20), fg='white')
length_label.pack(pady=5, anchor='center')
length_entry = tk.Entry(frame, width=20, font=('Arial', 18))
length_entry.pack(pady=5, anchor='center')

# Character Type Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar()

checkbox_frame = tk.Frame(frame, bg=style_bg)
checkbox_frame.pack(pady=13, anchor='center')

tk.Checkbutton(checkbox_frame, text="Include Uppercase (A-Z)", variable=var_upper, bg=style_bg, fg='white', selectcolor=style_bg).pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Include Lowercase (a-z)", variable=var_lower, bg=style_bg, fg='white', selectcolor=style_bg).pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Include Numbers (0-9)", variable=var_numbers, bg=style_bg, fg='white', selectcolor=style_bg).pack(anchor='w')
tk.Checkbutton(checkbox_frame, text="Include Symbols (@#$%)", variable=var_symbols, bg=style_bg, fg='white', selectcolor=style_bg).pack(anchor='w')

# Generate Button
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=('Arial', 12))
generate_button.pack(pady=15)

# Password Display
password_display = tk.Entry(frame, state='readonly', width=35, font=('Arial', 18), bg='black', fg='white')
password_display.pack(pady=5)

# Copy Button
copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=('Arial', 12))
copy_button.pack(pady=15)

root.mainloop()