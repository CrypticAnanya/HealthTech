from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",port="3306",password="admin",database="hospital")
cur=connection.cursor()
class DisplayDoctor:
    def data(self):
        if self.l.get():
            name = self.l.get()
        else:
            name = self.combo.get()

        q = "select * from add_doctor where Name=%s"
        cur.execute(q, (name,))
        data1 = cur.fetchall()
        IDentry = Label(self.root, text=data1[0][0],font=("Arial", 16), bg="white", fg="black").place(x=220, y=170)

        nameentry = Label(self.root,text=data1[0][1], font=("Arial", 16), bg="white", fg="black").place(x=220, y=210)
        emailentry = Label(self.root,text=data1[0][2], font=("Arial", 16), bg="white", fg="black").place(x=220, y=260)
        Phone_Numberentry = Label(self.root,text=data1[0][3], font=("Arial", 16), bg="white", fg="black").place(x=650, y=210)
        Age = Label(self.root,text=data1[0][7] ,font=("Arial", 16), bg="white", fg="black").place(x=650, y=300)
        gender = Label(self.root,text=data1[0][4] ,font=("Arial", 16), bg="white", fg="black").place(x=650, y=170)
        Departmententry = Label(self.root,text=data1[0][5], font=("Arial", 16), bg="white", fg="black").place(x=650, y=260)
        Positionentry = Label(self.root,text=data1[0][6], font=("arial", 16), bg="white", fg="black").place(x=220, y=300)
        Addressentry = Label(self.root,text=data1[0][8], font=("Arial", 16), bg="white", fg="black").place(x=220, y=350, width=680, height=90)



    def __init__(self, root):
        self.root = root
        self.root.geometry("970x520+350+130")
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg="white")
        self.root.focus_force()
        q="select * from add_doctor"
        cur.execute(q)
        data=cur.fetchall()
        c=0
        n=[]
        for i in data:
            c=c+1
            n.append(i[1])
        SearchFrame = LabelFrame(self.root, text="Search Doctor", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white").place(x=80, y=70, width=850, height=80)
        self.combo = ttk.Combobox(self.root,values=n)
        self.combo.place(x=100,y=100,width=400,height=35)
        self.l=Entry(self.root,font=('algerian',20))
        self.l.place(x=520,y=100,width=250)
        search = Button(self.root, text="Search :",command=self.data, font=("Arial", 16), bg="blue", fg="white").place(x=800,y=100)
        title = Label(self.root, text="Display Doctor", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white",padx=20).place(x=0, y=0, relwidth=1, height=70)
        ID = Label(self.root, text="ID", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=170, width=100)
        IDentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=170)
        name = Label(self.root, text="Name :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=210, width=100)
        nameentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=210)
        Gender = Label(self.root, text="Gender :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=170, width=140)
        combo = Label(self.root,font=("Arial", 16), bg="white", fg="black").place(x=650, y=170, width=240, height=30)
        email = Label(self.root, text="Email :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=260, width=100)
        emailentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=260)
        Phone_Number = Label(self.root, text="Phone No. :", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=210,width=140)
        Phone_Numberentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=210)
        Department = Label(self.root, text=" Department:", font=("Arial", 16), bg="blue", fg="white").place(x=500,y=260,width=140)
        Departmententry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=260)
        Position = Label(self.root, text="Position :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=300,width=100)
        Positionentry = Entry(self.root, font=("arial", 16), bg="white", fg="black").place(x=220, y=300)
        Age = Label(self.root, text=" Age:", font=("Arial", 16), bg="blue", fg="white").place(x=500, y=300, width=140)
        Ageentry = Entry(self.root, font=("Arial", 16), bg="white", fg="black").place(x=650, y=300)
        Address = Label(self.root, text="Address :", font=("Arial", 16), bg="blue", fg="white").place(x=100, y=350)
        Addressentry = Text(self.root, font=("Arial", 16), bg="white", fg="black").place(x=220, y=350, width=680, height=90)
        #btn_Submit = Button(self.root, text="Submit",command=self.data, font=("Arial", 15, "bold"), bg="Yellow", cursor="hand2").place(x=800, y=450, height=50, width=150)

if __name__=="__main__":
    root = Tk()
    obj = DisplayDoctor(root)
    root.mainloop()
