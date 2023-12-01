import tkinter as tk

def convert_temperature():
    try:
        # Get the temperature value from the entry widget
        input_temp = float(entry.get())

        # Check the selected input and output units
        input_unit = unit_options[input_unit_var.get()]
        output_unit = unit_options[output_unit_var.get()]

        # Perform the conversion
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = (input_temp * 9/5) + 32
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = input_temp + 273.15
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = (input_temp - 32) * 5/9
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            result = (input_temp - 32) * 5/9 + 273.15
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = input_temp - 273.15
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            result = (input_temp - 273.15) * 9/5 + 32
        else:
            result = input_temp # If same units are selected

        output_label.config(text=f"Converted: {result:.2f} {output_unit}")
    except ValueError:
        output_label.config(text="Invalid input. Enter a numeric value.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Temperature input
tk.Label(window, text="Enter Temperature:").pack()
entry = tk.Entry(window)
entry.pack()

# Unit options
unit_options = {1: "Celsius", 2: "Fahrenheit", 3: "Kelvin"}

# Input unit selection
tk.Label(window, text="Select Input Unit:").pack()
input_unit_var = tk.IntVar()
for unit_num, unit_name in unit_options.items():
    tk.Radiobutton(window, text=unit_name, variable=input_unit_var, value=unit_num).pack()

# Output unit selection
tk.Label(window, text="Select Output Unit:").pack()
output_unit_var = tk.IntVar()
for unit_num, unit_name in unit_options.items():
    tk.Radiobutton(window, text=unit_name, variable=output_unit_var, value=unit_num).pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
convert_button.pack()

# Output label
output_label = tk.Label(window, text="")
output_label.pack()

# Start the Tkinter event loop
window.mainloop()