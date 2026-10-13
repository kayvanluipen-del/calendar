from tkinter import *
import calendar

gui = Tk()
gui.config(background="white")
gui.title("CALENDAR")
gui.geometry("400x300")


def showcal():

    new_gui=Tk()
    new_gui.config(background="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("600x600")

    entered_year=int(year_input.get())
    display_calendar=calendar.calendar(entered_year)
    calendar_label= Label(new_gui, text=display_calendar,font="Consolas 10 bold")
    calendar_label.grid(row=5,column=2, padx=20)

    new_gui.mainloop()


calendar1 = Label(gui,text="CALENDAR",bg="dark grey",font=("times",28,"bold"))
year = Label(gui,text="YEAR",bg="light grey",font=("times",18,"bold"))

year_input = Entry()

show_calendar = Button(gui,text="show Calendar",fg="black",bg="blue", command=showcal)

exit = Button(gui,text="EXIT",fg="black",bg="red",command=gui.destroy)



calendar1.grid(row=1,column=1)
year.grid(row=3,column=1)
year_input.grid(row=5,column=1)
show_calendar.grid(row=7,column=1)
exit.grid(row=9,column=1)











gui.mainloop()