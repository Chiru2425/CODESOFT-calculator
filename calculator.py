import tkinter as tk

# Function to perform mathematical operations
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

# Function to add characters to the input field
def add_to_input(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + char)

# Function to clear the input field
def clear_input():
    entry.delete(0, tk.END)

# Create a Tkinter window
window = tk.Tk()
window.title(" Calculator")

# Entry field for input
entry = tk.Entry(window, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Result label
result = tk.StringVar()
result.set("")
result_label = tk.Label(window, textvariable=result, font=("Arial", 20))
result_label.grid(row=1, column=0, columnspan=4)

# Buttons for calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 2
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 20),
              command=lambda b=button: add_to_input(b) if b != '=' else evaluate_expression()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(window, text="C", padx=20, pady=20, font=("Arial", 20), command=clear_input)
clear_button.grid(row=row_val, column=col_val)

# Start the Tkinter main loop
window.mainloop()
