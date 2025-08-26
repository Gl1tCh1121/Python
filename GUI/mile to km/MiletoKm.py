from tkinter import *

def button_clicked():
    print("Calculated")
    new_text = int(input.get())
    calc_text.config(text=new_text*1.6)

window = Tk()
window.title("Mile to Km")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


#  Widgets

text1 = Label(text="Is equal to", font=("Arial", 16, "bold"))
text1.grid(column=0, row=1)

text2 = Label(text="KM", font=("Arial", 18, "bold"))
text2.grid(column=2, row=1)

calc_text = Label(text="calculated miles", font=("Arial", 16, "bold"))
calc_text.config(text="0")
calc_text.grid(column=1, row=1)

button = Button(text="Calculate", font=("Arial", 14, "bold"), command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=18)
print(input.get())
input.grid(column=1, row=0)







window.mainloop()