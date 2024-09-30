from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

db = mysql.connector.connect(user ='root', host='localhost',port= '3306', password = 'admin', database = 'hospital')
cur = db.cursor()


class DisplayAppointment:

    def __init__(self, root):
        self.root = root
        self.root.geometry("900x520+350+130")
        self.root.resizable(False,False)
        self.root.title("HEALTH TECHNOLOGY SYSTEM | Developed By WARRIORS")
        self.root.config(bg = "white")
        self.root.focus_force()
        title = Label(self.root, text="Display Appointment", font=("ALGERIAN", 40, "bold"), bg="blue", fg="white",padx=20).place(x=0, y=0, relwidth=1, height=70)
        Label(self.root,text="Appointments Scheduled",font=("Algerian",30,"bold"),bg="white",fg="blue",padx=20).place(x=20,y=70,relwidth=1,height=70)

        treev = ttk.Treeview(self.root, selectmode='browse')
        treev.pack(side='left')
        verscrlbar = ttk.Scrollbar(self.root,orient="vertical",command=treev.yview)
        verscrlbar.pack(side='right', fill='x')
        treev.configure(xscrollcommand=verscrlbar.set)
        treev["columns"] = ("1", "2", "3","4","5","6","7","8","9")
        treev['show'] = 'headings'
        treev.column("1", width=100, anchor='c')
        treev.column("2", width=90, anchor='se')
        treev.column("3", width=120, anchor='se')
        treev.column("4", width=90, anchor='se')
        treev.column("5", width=90, anchor='se')
        treev.column("6", width=90, anchor='se')
        treev.column("7", width=90, anchor='se')
        treev.column("8", width=90, anchor='se')
        treev.column("9", width=90, anchor='se')

        treev.heading("1", text="Appointment_No")
        treev.heading("2", text="Patient_Name")
        treev.heading("3", text="Email")
        treev.heading("4", text="Time")
        treev.heading("5", text="Phone_No")
        treev.heading("6", text="Gender")
        treev.heading("7", text="Date")
        treev.heading("8", text="Age")
        treev.heading("9", text="Address")





        q="select * from book_appointment"
        cur.execute(q)
        data=cur.fetchall()
        for i in data:
            treev.insert("", 'end', text="L1", values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))


if __name__=="__main__":
    root = Tk()
    obj = DisplayAppointment(root)
    root.mainloop()
