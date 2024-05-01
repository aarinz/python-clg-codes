from tkinter import *

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100 
    bmi = weight / (height * height)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

    if bmi < 18:
        result_label.config(text="Underweight")
    elif 18 <= bmi < 25:
        result_label.config(text="Normal")
    elif 25 <= bmi < 30:
        result_label.config(text="Overweight")
    else:
        result_label.config(text="Obese")

window = Tk()
window.title("BMI Calculator")

weight_label = Label(window, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

weight_entry = Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = Label(window, text="Height (cm):")
height_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

height_entry = Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = Button(window, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

bmi_label = Label(window, text="BMI:")
bmi_label.grid(row=3, columnspan=2)

result_label = Label(window, text="")
result_label.grid(row=4, columnspan=2)

window.mainloop()
