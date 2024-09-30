from tkinter import *
from PIL import Image, ImageTk
from Add_Patient import AddPatient
from Add_Doctor import AddDoctor
from Book_Appointment import BookAppointment
from Display_Doctor import DisplayDoctor
from Display_Patient import DisplayPatient
from Pending_Patient import PendingPatient
from Display_Appointment import DisplayAppointment
import datetime as dt
from time import strftime
time_string = strftime('%H:%M:%S %p')
date = dt.datetime.now()
class health:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg="white")
        self.icon_title = PhotoImage(file="IMAGES/logo (2).png")
        title=Label(self.root, text="HEALTH TECHNOLOGY SYSTEM", image=self.icon_title, compound=LEFT, font=("ALGERIAN",40,"bold"), bg="blue", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)
        btn_logout=Button(self.root, text="Logout", font=("Arial", 15, "bold"),command=self.out, bg="Yellow", cursor="hand2").place(x=1170, y=10, height=50, width=150)
        self.label_clock = (Label(self.root, text=f"WELCOME TO HEALTH TECHNOLOGY SYSTEM\t\tDate:{date: %B %d, %Y} \t\t Time: %s"%(time_string), font=("Arial", 15), bg="GREY", fg="white").place(x=0, y=70, relwidth=1, height=30))
        self.Menu_Logo = Image.open("IMAGES/logo.png")
        self.Menu_Logo = self.Menu_Logo.resize((100, 100))
        self.Menu_Logo = ImageTk.PhotoImage(self.Menu_Logo)
        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftMenu.place(x=0, y=102, width=350, height=565)
        Label_menuLogo = Label(leftMenu, image=self.Menu_Logo)
        Label_menuLogo.pack(side=TOP, fill=X)
        self.icon_side = PhotoImage(file="IMAGES/side.png")
        label_menu=Label(leftMenu, text="Menu", font=("times new roman", 20), bg="Green").pack(side=TOP, fill=X)

        button_Add_Patient=Button(leftMenu, text="Add Patients",command=self.AddPatient,image = self.icon_side, compound = LEFT,padx = 5, anchor = "w", font=("times new roman", 20, "bold"), bg="white", bd = 3, cursor = "hand2").pack(side=TOP, fill=X)
        button_Add_Doctors=Button(leftMenu, text="Add Doctors", command=self.AddDoctor, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        button_Book_Appointment=Button(leftMenu, text="Book Appointment", command=self.BookAppointment, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        button_Pending_Patient=Button(leftMenu, text="Pending Patient", command=self.PendingPatient, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        button_Display_Patient=Button(leftMenu, text="Display Patient", command=self.DisplayPatient, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        button_Display_Doctor=Button(leftMenu, text="Display Doctor", command=self.DisplayDoctor, image=self.icon_side, compound=LEFT, padx=5, anchor="w",font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        button_Display_Appointment=Button(leftMenu, text="Display Appointment", command=self.DisplayAppointment, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        self.label_Add_Shows = Label(self.root, text="Total Patients\n[ 0 ]", bd=5, relief=RIDGE, bg="blue", fg="white",font=("goudy old style", 20, "bold"))
        self.label_Add_Shows.place(x=400, y=150, height=150, width=400)
        self.label_Add_Snacks = Label(self.root, text="Pending Patients\n[ 0 ]", bd=5, relief=RIDGE, bg="blue", fg="white", font=("goudy old style", 20, "bold"))
        self.label_Add_Snacks.place(x=900, y=150, height=150, width=400)
        self.label_Book_Ticket = Label(self.root, text="Total Doctors\n[ 0 ]", bd=5, relief=RIDGE, bg="blue", fg="white", font=("goudy old style", 20, "bold"))
        self.label_Book_Ticket.place(x=650, y=400, height=150, width=400)
        label_Footer = Label(self.root, text="WELCOME TO HEALTH TECHNOLOGY SYSTEM | Developed By Team Warriors\n For any Technical Issue Contact: 7011722230", font=("Arial", 12), bg="GREY", fg="white").pack(side = BOTTOM, fill = X)
    def AddPatient(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AddPatient(self.new_win)
    def AddDoctor(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=AddDoctor(self.new_win)
    def BookAppointment(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BookAppointment(self.new_win)
    def DisplayAppointment(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=DisplayAppointment(self.new_win)
    def DisplayDoctor(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=DisplayDoctor(self.new_win)
    def DisplayPatient(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=DisplayPatient(self.new_win)
    def PendingPatient(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=PendingPatient(self.new_win)
    def out(self):
        exit(0)


if __name__=="__main__":
    root = Tk()
    obj = health(root)
    root.mainloop()

