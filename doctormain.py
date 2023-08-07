import re
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
import csv
import main
import DLL, dequeagain
import doctormain,invoice
from dequeagain import Deque

class Doctor:        
    def __init__(self,doctor):
        def logoutf():
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                self.sel.clear()
                self.doctor.destroy()
                main.page()

        def exitf():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=doctor)
            if sure == True:
                #self.sel.clear()
                self.doctor.destroy()
        
        self.doctor=doctor
        doctor.geometry("1366x768")
        doctor.resizable(0, 0)
        doctor.title("Doctor Main")

        self.label1 = Label(doctor)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/docmain.png")
        self.label1.configure(image=self.img)

        self.button2 = Button(doctor)
        self.button2.place(relx=0.056, rely=0.095, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#3047ff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#3047ff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=logoutf)

        self.button6 = Button(doctor)
        self.button6.place(relx=0.901, rely=0.095, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#3047ff")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#3047ff")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(command=exitf)

        self.scrollbarx = Scrollbar(doctor, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(doctor, orient=VERTICAL)
        self.tree = ttk.Treeview(doctor)
        self.tree.place(relx=0.038, rely=0.22, width=790, height=500)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set )
        self.tree.configure(selectmode="extended")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.615, rely=0.222, width=22, height=498)
        self.scrollbarx.place(relx=0.038, rely=0.870, width=810, height=22)

        #Reg No	Name	Age	Gender	Phone No	Email	Detailed Medical History	Prescription

        self.tree.configure(
            columns=(
                "Name",
                "Age",
                "Gender",
                "Phone No.",
                "Email",
                #"Detailed Medical History",
                #"Prescription"
                ))
        
        
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Age", text="Age", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)
        self.tree.heading("Phone No.", text="Phone No.", anchor=W)
        self.tree.heading("Email", text="Email", anchor=W)
        #self.tree.heading("Detailed Medical History", text="Detailed Medical History", anchor=W)
        #self.tree.heading("Prescription", text="Prescription", anchor=W)
        

        self.tree.column("#0", stretch=YES, minwidth=0, width=-50)
        self.tree.column("#1", stretch=YES, minwidth=0, width=70)
        self.tree.column("#2", stretch=YES, minwidth=0, width=30)
        self.tree.column("#3", stretch=YES, minwidth=0, width=45)
        self.tree.column("#4", stretch=YES, minwidth=0, width=70)
        #self.tree.column("#5", stretch=YES, minwidth=0, width=140)
        #self.tree.column("#6", stretch=YES, minwidth=0, width=200)
        
        self.DisplayDetails()
        
        #-------------medical his----------------------------------
       
        def temp_text1(e):
            self.Text_box1.delete(0.0,"end")
        
        def temp_text2(e):
            self.Text_box2.delete(0.0,"end")

        self.Text_box1 = Text(self.doctor, font=("default", 15))
        self.Text_box1.place(relx=0.66, rely=0.28,height = 140, width = 392)
        self.Text_box1.insert(0.0,"Add Diagnosis...")
        self.Text_box1.bind("<FocusIn>",temp_text1)

        self.Text_box2 = Text(self.doctor, font=("default", 15))
        self.Text_box2.place(relx=0.66, rely=0.51,height = 140, width = 392)
        self.Text_box2.insert(0.0,"Enter prescription...")
        self.Text_box2.bind("<FocusIn>", temp_text2)

        self.back_button_label = Button(self.doctor, text='VIEW HISTORY', font=("gotham", 10, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.update_emp)
        self.back_button_label.place(relx=0.75, rely=0.78, width=140, height=25)    

        self.back_button_label = Button(self.doctor, text='ADD', font=("gotham", 10, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.add)
        self.back_button_label.place(relx=0.75, rely=0.73, width=140, height=25) 

        self.back_button_label = Button(self.doctor, text='END CONSULTATION', font=("gotham", 10, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.endcon)
        self.back_button_label.place(relx=0.741, rely=0.8350, width=170, height=25)
            #relx=0.755, rely=0.8350, width=140, height=25) 
       
    def DisplayDetails(self):
        global acc
        f=open("patientqueue.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree.insert("", "end", values=(data))
        #-------focus first-----

        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
        
        self.tree.selection_set(val[0])
        self.tree.focus(val[0])

    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def update_emp(self):
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
        
            if len(self.sel)==1:
                self.doctor.destroy()
                global e_update
                e_update = Tk()
                page8 = Update_Employee(e_update)
            
                e_update.mainloop()
            
            elif len(self.sel)==0:
                messagebox.showerror("Error","Please select an patient to view.")
            else:
                messagebox.showerror("Error","Can only view one patient at a time.")
   
    def add(self):
        global vall
        vall=[]
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        self.add_details()
        
    
    def add_details(self):
        global x,y
        x = self.Text_box1.get(0.0, "end-1c")
        y = self.Text_box2.get(0.0, "end-1c")
        if len(self.sel)==0:
            pass
        else:
            p = vall.pop(5)
            q = vall.pop(5)
                
            a = p+" \n\n"+x
            b = q+" \n\n"+y
                
            vall.append(a) 
            vall.append(b)
            f=open("patientqueue.csv","r")
            a=csv.reader(f)
            acc=[]    
        
            for row in a:
                acc.append(row)
            acc[0]=vall
                
            f=open("patientqueue.csv","w",newline="")
            a=csv.writer(f)
            a.writerows(acc)
            f.close()
            
            f=open("patientrecord.csv","r",newline="")
            
            reading = csv.reader(f)
            rec = []
            for i in reading:
                rec.append(i)
            
            #print(rec)
            for j in acc:
                for i in rec:
                    if j[0] == i[0]:
                        rec[rec.index(i)] = j
            
            #print(rec)
            f1=open("patientrecord.csv","w",newline="")
            writerobj = csv.writer(f1)
            writerobj.writerows(rec)
            f1.close()
            f.close()
            messagebox.showinfo("Success!!", "Diagnosis and Prescription updated in database.", parent=self.doctor)
            self.Text_box1.delete(0.0,END)
            self.Text_box2.delete(0.0,END)
            self.tree.delete(*self.tree.get_children())
            self.DisplayDetails()
            return vall

    def endcon(self):
        global vall
        vall=[]
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        self.end_con()

    def end_con(self):
        f = open('patientqueue.csv', 'r')
        a=csv.reader(f)
         
        queueobj = Deque()

        for row in a:
            queueobj.insert_last(row)

        queueobj.delete_first()

        x = queueobj.__str__()
        f=open("patientqueue.csv","w",newline="")
        a=csv.writer(f)
        a.writerows(x)
        f.close()

        messagebox.showinfo("Success!!", "Consultation is over.", parent=self.doctor)
        self.tree.delete(*self.tree.get_children())
        self.DisplayDetails()
        self.doctor.destroy()
        invoice.page()  

class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Patient History")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/viewpatient.png")
        self.label1.configure(image=self.img)

        def exitf():
            e_update.destroy()
            doctormain.page()

        self.back_button_label = Button(e_update, text='BACK', font=("gotham", 13, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=exitf)
        self.back_button_label.place(relx=0.4675, rely=0.844, width=100, height=35)

        self.entry1 = Label(e_update,text=vall[0])
        self.entry1.place(relx=0.122, rely=0.270)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry1 = Label(e_update,text=vall[1])
        self.entry1.place(relx=0.124, rely=0.500)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry1 = Label(e_update,text=vall[2])
        self.entry1.place(relx=0.120, rely=0.615)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry1 = Label(e_update,text=vall[3])
        self.entry1.place(relx=0.124, rely=0.385)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry1 = Label(e_update,text=vall[4])
        self.entry1.place(relx=0.120, rely=0.730)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry1 = Text(e_update)
        self.entry1.insert(INSERT,vall[5])
        self.entry1.place(relx=0.547, rely=0.320,width=455,height=122)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='white',fg='black',state=DISABLED)
        self.entry1.configure(relief="flat")
        
        self.entry1 = Text(e_update)
        self.entry1.insert(INSERT,vall[6])
        self.entry1.place(relx=0.547, rely=0.562,width=455,height=136)
        self.entry1.configure(font=("gotham", 13, "bold"),bg='white',fg='black',state=DISABLED)
        self.entry1.configure(relief="flat") 
        


def page():
    doctor = Tk()
    Doctor(doctor)
    doctor.mainloop()


if __name__ == '__main__':
    page()