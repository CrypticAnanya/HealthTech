from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

db = mysql.connector.connect(user ='root', host='localhost',port= '3306', password = 'admin', database = 'hospital')
cur = db.cursor()

#These command is use for create table
#query = 'use hospital'
##cur.execute(query)
#query = "create table book_appointment(Appointment_No varchar(20), Patient_Name varchar(30), Email varchar(30), Time varchar(30), PhoneNo varchar(20),Gender varchar(30), Date varchar(30),Age varchar(30), Address varchar(30))"
#cur.execute(query)


class BookAppointment:
    def insert(self):
        query = "insert into book_appointment(Appointment_No, Patient_Name, Email, Time, PhoneNo, Gender, Date, Age, Address )values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            self.Appointment_Noentry.get(),self.Patient_Nameentry.get(), self.emailentry.get(),
            self.Timeentry.get(), self.Phone_Numberentry.get(),self.combo.get(),
            self.Dateentry.get(),self.Ageentry.get(), self.Addressentry.get(0.1,END))
        cur.execute(query,val)
        db.commit()
        messagebox.showinfo("Submit", "Submitted Successfully")


    def __init__(self,root):
        self.root = root
        self.root.geometry("970x520+350+130")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg="white")
        self.root.focus_force()
        title = Label(self.root, text="Book Appointment", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white",padx=20).place(x=0, y=0, relwidth=1, height=70)

        Appointment_No = Label(self.root, text="Appointment No.:", font=("Arial", 16), bg="blue", fg="white").place(x=40, y=120, width=160)
        self.Appointment_Noentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Appointment_Noentry.place(x=220, y=120)

        Patient_Name = Label(self.root, text="Patient Name :", font=("Arial", 16), bg="blue", fg="white").place(x=40, y=170, width=160)
        self.Patient_Nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Patient_Nameentry.place(x=220, y=170)

        Gender = Label(self.root, text="Gender :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=170, width=140)
        self.combo = ttk.Combobox(self.root, values=['Male', 'Female'])
        self.combo.place(x=650, y=170, width=240, height=30)

        email = Label(self.root, text="Email :", font=("Arial", 16), bg="blue", fg="white").place(x=40, y=220, width=160)
        self.emailentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.emailentry.place(x=220, y=220)

        Phone_Number = Label(self.root, text="Phone No. :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=120, width=140)
        self.Phone_Numberentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Phone_Numberentry.place(x=650, y=120)

        Date = Label(self.root, text=" Date:", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=220, width=140)
        self.Dateentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Dateentry.place(x=650, y=220)

        Time = Label(self.root, text="Time :", font=("Arial", 16), bg="blue", fg="white").place(x=40, y=270, width=160)
        self.Timeentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Timeentry.place(x=220, y=270)

        Age = Label(self.root, text=" Age:", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=270, width=140)
        self.Ageentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Ageentry.place(x=650, y=270)

        Address = Label(self.root, text="Address :", font=("Arial", 16), bg="blue", fg="white").place(x=40, y=320, width=160)
        self.Addressentry = Text(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Addressentry.place(x=220, y=320, width=680, height=100)

        btn_Submit = Button(self.root, text="Submit", font=("Arial", 15, "bold"), bg="Yellow", command=self.insert,cursor="hand2").place( x=800, y=450, height=50, width=150)

if __name__=="__main__":
    root = Tk()
    obj = BookAppointment(root)
    root.mainloop()
