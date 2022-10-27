from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(pady=100, padx=100)

# Label
miles = Label(text="Miles", font=("Ariel", 25))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Ariel", 25))
km.grid(column=2, row=1)

equal_to = Label(text="is equal to", font=("Ariel", 25))
equal_to.grid(column=0, row=1)

answer = Label(text="0", font=("Ariel", 25))
answer.grid(column=1, row=1)


# Button
def button_clicked():
    new_input = round(int(milage.get()) / 1.609,2)
    answer.config(text=f"{new_input}")


calculate = Button(text='Calculate', font=("Ariel", 25), command=button_clicked)
calculate.grid(column=1, row=2)
#Entry
milage = Entry(width=30)
milage.grid(column=1, row=0)

window.mainloop()
