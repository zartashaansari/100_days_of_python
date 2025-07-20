from tkinter import *
VALUE=1.6093
window=Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=100,height=100)
window.config(padx=50,pady=50)
enter_miles=Entry(width=10)
enter_miles.grid(row=2,column=2)
answer_label=Label(text="0")
answer_label.grid(row=3,column=2)
def button_action():
    miles=int(enter_miles.get())
    kilometer=miles*VALUE
    answer_label.config(text=f"{kilometer:.2f}")


label_miles=Label(text="Miles")
label_miles.grid(row=2,column=3)
label_km=Label(text="km")
label_km.grid(row=3,column=3)
label_equal=Label(text="Is equal to")
label_equal.grid(row=3,column=1)
button=Button(text="Convert",command=button_action)
button.grid(row=4,column=2)















window.mainloop()