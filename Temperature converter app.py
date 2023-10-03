import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, str(fahrenheit))
    except ValueError:
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, "Invalid input")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, str(celsius))
    except ValueError:
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, "Invalid input")

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x150")

# Celsius to Fahrenheit
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0)
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1)
button_celsius_to_fahrenheit = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_celsius_to_fahrenheit.grid(row=0, column=2)

# Fahrenheit to Celsius
label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(row=1, column=0)
entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=1, column=1)
button_fahrenheit_to_celsius = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_fahrenheit_to_celsius.grid(row=1, column=2)

root.mainloop()
