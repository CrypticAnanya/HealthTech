
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector



db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', port='3306', database ='hospital')
cur = db.cursor()


#These command is use for create table
#query = 'use hospital'
#cur.execute(query)
#query = 'create table add_doctor(ID varchar(80), Name varchar(80), Email varchar(80), Phone_Number varchar(30), Gender varchar(30), Department varchar(30), Position varchar (30), Age int , Address  varchar(30))'
#cur.execute(query)



class AddDoctor:
    def insert (self):
        query = "insert into add_doctor(Id, Name, Email, Phone_Number, Gender, Department, Position, Age, Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            self.IDentry.get(), self.Nameentry.get(), self.Emailentry.get(), self.Phone_Numberentry.get(), self.combo.get(),
            self.Departmententry.get(),
            self.Positionentry.get(), self.Ageentry.get(), self.Addressentry.get(1.0,END))
        cur.execute(query, val)
        db.commit()
        messagebox.showinfo("Submit", "Submitted Successfully")


    def __init__(self, root):
        self.root = root
        self.root.geometry("970x520+350+130")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg = "white")
        self.root.focus_force()

        title = Label(self.root, text="ADD DOCTOR", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white", padx=20).place(x=0, y=0, relwidth=1, height=70)

        ID = Label(self.root, text="ID", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=120,width=100)
        self.IDentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.IDentry.place(x=220, y=120)


        Name = Label(self.root, text="Name :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=170, width=100)
        self.Nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Nameentry.place(x=220, y=170)

        Gender = Label(self.root, text="Gender :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=170,width=140)
        self.combo = ttk.Combobox(self.root, values=['Male', 'Female'])
        self.combo.place(x=650, y=170, width=240, height=30)

        Email = Label(self.root, text="Email :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=220, width=100)
        self.Emailentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Emailentry.place(x=220, y=220)

        Phone_Number = Label(self.root, text="Phone No. :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=120, width=140)
        self.Phone_Numberentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Phone_Numberentry.place(x=650, y=120)

        Department = Label(self.root, text=" Department:", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=220, width=140)
        self.Departmententry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Departmententry.place(x=650, y=220)

        Position = Label(self.root, text="Position :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=270, width=100)
        self.Positionentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Positionentry.place(x=220, y=270)

        Age = Label(self.root, text=" Age:", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=270, width=140)
        self.Ageentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Ageentry.place(x=650, y=270)

        Address = Label(self.root, text="Address :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=320)
        self.Addressentry = Text(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Addressentry.place(x=220, y=320, width=680,height=100)



        btn_Submit = Button(self.root, text="Submit", font=("Arial", 15, "bold"), bg="Yellow",command= self.insert, cursor="hand2").place(x=800, y=450, height=50, width=150)


if __name__ == "__main__":
    root = Tk()
    obj = AddDoctor(root)
    root.mainloop()
