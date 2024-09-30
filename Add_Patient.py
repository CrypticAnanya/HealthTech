from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(user='root', host='localhost', port='3306', password='admin', database='hospital')
cur = db.cursor()

#These command is use for create table
#query = 'use hospital'
#cur.execute(query)
#query = 'create table add_patient(PatientID varchar(30),Name varchar(30),Email varchar(30), Age varchar(30),PhoneNO varchar(30), Gender varchar(30), Disease varchar(30),Doctor_Name varchar (50),Address varchar(50))'
#cur.execute(query)



class AddPatient():

    def insert(self):
        patient_id=self.PatientIDentry.get()
        name=self.Nameentry.get()
        query = "insert into add_patient(PatientID, Name, Email, Age, PhoneNO, Gender, Disease, Doctor_Name ,Address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (patient_id,name,self.Emailentry.get(),self.Ageentry.get(),self.Phone_Numberentry.get(), self.combo.get(), self.Diseaseentry.get(),self.Doctor_Nameentry.get(), self.Addressentry.get(0.1, END))
        cur.execute(query, val)
        db.commit()
        messagebox.showinfo("Submit", "Submitted Successfully")

    def __init__(self, root):
        self.root = root
        self.root.geometry("970x520+350+130")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg="white")
        self.root.focus_force()

        title = Label(self.root, text="Add Patient", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white", padx=20).place(x=0, y=0, relwidth=1, height=70)


        PatientID = Label(self.root,text="Patient ID",font=("Arial", 16), bg="blue", fg="white").place(x=100, y=120, width=100)
        self.PatientIDentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.PatientIDentry.place(x=220, y=120)

        Name = Label(self.root, text="Name :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=170, width=100)
        self.Nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Nameentry.place(x=220, y=170)

        Gender = Label(self.root, text="Gender :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=170, width=140)
        self.combo = ttk.Combobox(self.root, values=['Male', 'Female'])
        self.combo.place(x=650,y=170,width=240,height=30)

        Age = Label(self.root, text="Age :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=270, width=100)
        self.Ageentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Ageentry.place(x=220, y=270)

        Doctor_Name = Label(self.root, text="Doctor Name :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=270, width=140)
        self.Doctor_Nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Doctor_Nameentry.place(x=650, y=270)


        Email = Label(self.root, text="Email :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=220, width=100)
        self.Emailentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Emailentry.place(x=220, y=220)

        Phone_Number = Label(self.root, text="Phone No. :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=120,width=140)
        self.Phone_Numberentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Phone_Numberentry.place(x=650, y=120)

        Disease = Label(self.root, text="Disease :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=220,width=140)
        self.Diseaseentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Diseaseentry.place(x=650, y=220)

        Address = Label(self.root, text="Address :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=320)
        self.Addressentry = Text(self.root, font=("Arial", 16), bg="white", fg="black")
        self.Addressentry.place(x=220, y=320, width=680, height= 100)

        btn_Submit = Button(self.root, text="Submit", font=("Arial", 15, "bold"), bg="Yellow",command=self.insert, cursor="hand2").place(x=800, y=450, height=50, width=150)
        btn_Receipt = Button(self.root, text="Receipt", font=("Arial", 15, "bold"), bg="Yellow", cursor="hand2").place(x=100, y=450, height=50, width=150)

if __name__ == "__main__":
    root = Tk()
    obj = AddPatient(root)
    root.mainloop()
