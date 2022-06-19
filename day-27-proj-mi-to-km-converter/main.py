from tkinter import *
STARTING_USER_INPUT = 0
BUTTON_TEXT = "Calculate!"


def calculate():
    user_input = float(miles_entry.get())
    km = round(user_input * 1.609, 1)
    result.config(text=f"{km}")


# setup window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

# entry box input for miles
miles_entry = Entry(width=8, text="0")
# miles_entry.config(padx=10, pady=10
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# conversion text
result_prefix = Label(text="is equal to")
result_prefix.grid(column=0, row=1)

result = Label(text=STARTING_USER_INPUT)
result.grid(column=1, row=1)

result_suffix = Label(text="Km")
result_suffix.grid(column=2, row=1)

# button
calc_button = Button(text=BUTTON_TEXT, command=calculate)
calc_button.grid(column=1, row=2)


# end program
window.mainloop()
