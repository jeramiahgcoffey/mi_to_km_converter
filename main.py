from tkinter import *
FONT = ("Arial", 16)

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=150)
window.config(padx=15, pady=50)

mi_input = Entry(width=7)
mi_input.grid(row=0, column=1)


def calculate():
    miles = float(mi_input.get())
    answer = round(miles * 1.609344, 2)
    answer_label.config(text=answer)


mi_label = Label(text="Miles", font=FONT)
mi_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

answer_label = Label(text="0", font=FONT)
answer_label.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)

window.mainloop()