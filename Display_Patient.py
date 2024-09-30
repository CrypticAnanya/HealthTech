from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",port="3306",password="admin",database="hospital")
cur=connection.cursor()
class DisplayPatient:
    def data(self):
        if self.l.get():
            name = self.l.get()
        else:
            name = self.combo.get()

        q = "select * from add_patient where Name=%s"
        cur.execute(q, (name,))
        data1 = cur.fetchall()

        PatientIDentry = Label(self.root, text=data1[0][0],font=("Arial", 16), bg="white", fg="black").place(x=220, y=160)
        genderentry = Label(self.root,text=data1[0][5], font=("Arial", 16), bg="white", fg="black") .place(x=650, y=160, width=240, height=30)
        nameentry = Label(self.root,text=data1[0][1], font=("Arial", 16), bg="white", fg="black").place(x=220, y=200)
        Phone_Numberentry = Label(self.root,text=data1[0][4], font=("Arial", 16), bg="white", fg="black").place(x=650, y=200)
        Ageentry = Label(self.root,text=data1[0][3], font=("Arial", 16), bg="white", fg="black").place(x=220, y=280)
        Doctor_Nameentry = Label(self.root,text=data1[0][7], font=("Arial", 16), bg="white", fg="black").place(x=650, y=280)
        Diseaseentry = Label(self.root,text=data1[0][6], font=("Arial", 16), bg="white", fg="black").place(x=650, y=240)
        Emailentry = Label(self.root,text=data1[0][2], font=("Arial", 16), bg="white", fg="black").place(x=220, y=240)
        Addressentry = Label(self.root,text=data1[0][8], font=("Arial", 16), bg="white", fg="black").place(x=220, y=360, width=680,height=80)


    def __init__(self, root):
        self.root = root
        self.root.geometry("970x520+350+130")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg="white")
        self.root.focus_force()
        q="select * from add_patient"
        cur.execute(q)
        data=cur.fetchall()
        c=0
        n=[]
        for i in data:
            c=c+1
            n.append(i[1])
        SearchFrame = LabelFrame(self.root, text="Search Patient", font=("goudy old style", 12, "bold"), bd=2,relief=RIDGE, bg="white").place(x=80, y=70, width=850, height=80)
        self.combo = ttk.Combobox(self.root, values=n)
        self.combo.place(x=100, y=100, width=400, height=35)
        self.l=Entry(self.root,font=('algrian',20))
        self.l.place(x=520,y=100,width=250)
        title = Label(self.root, text="Display Patient", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white", padx=20).place(x=0, y=0, relwidth=1, height=70)
        search=Button(self.root, text="Search :", font=("Arial", 16),command=self.data, bg="blue", fg="white").place(x=800,y=100)
        PatientID = Label(self.root, text="Patient ID", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=160, width=100)
        PatientIDentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=160)
        Gender = Label(self.root, text="Gender :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=160, width=140)
        genderentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black") .place(x=650, y=160, width=240, height=30)
        name = Label(self.root, text="Name :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=200, width=100)
        nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=200)
        #Price = Label(self.root, text="Price :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=320,width=100)
        #Priceentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=320)
        Phone_Number = Label(self.root, text="Phone No. :", font=("Arial", 16), bg="blue", fg="white").place(x=500,y=200,width=140)
        Phone_Numberentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=200)
        Age = Label(self.root, text="Age :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=280, width=100)
        Ageentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=280)
        Doctor_Name = Label(self.root, text="Doctor Name :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=280, width=140)
        Doctor_Nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=280)
        Disease = Label(self.root, text="Disease :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=240,width=140)
        Diseaseentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=240)
        Email = Label(self.root, text="Email :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=240,width=100)
        Emailentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=240)
        #Status = Label(self.root, text="Status :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=320, width=140)
        #combo = ttk.Combobox(self.root, values=['Pending', 'Completing', 'Completed']).place(x=650, y=320, width=240, height=30)
        Address = Label(self.root, text="Address :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=360,width=100)
        Addressentry = Text(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=360, width=680,height=80)
        #btn_Submit = Button(self.root, text="Submit",command=self.data, font=("Arial", 15, "bold"), bg="Yellow", cursor="hand2").place( x=800, y=450, height=50, width=150)

if __name__=="__main__":
    root = Tk()
    obj = DisplayPatient(root)
    root.mainloop()