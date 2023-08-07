import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
import csv
import main
import re
from dequeagain import Deque

def valid_phone(phn):
    if phn.isdigit() and len(phn)==10:
        return True
    return False

class Employee:
    def __init__(self, emp):
        
        self._que = Deque()
        self._queuelimit = 4
        def logoutf():
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                self.sel.clear()
                self.emp.destroy()
                main.page()

        def exitf():
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=emp)
            if sure == True:
                self.sel.clear()
                self.emp.destroy()

          
            
        self.emp=emp
        emp.geometry("1366x768")
        emp.resizable(0, 0)
        emp.title("Patient Management")

        
        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/clinic.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(emp)
        self.entry1.place(relx=0.04, rely=0.28, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")

        self.button1 = Button(emp)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#3047ff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_emp)

        self.button2 = Button(emp)
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

        self.button3 = Button(emp)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#3047ff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#3047ff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD PATIENT TO DB""")
        self.button3.configure(command=self.add_emp)

        self.button4 = Button(emp)
        self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#3047ff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#3047ff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""ADD PATIENT TO QUEUE""")
        self.button4.configure(command=self.update_emp)

        """ self.button5 = Button(emp)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#3047ff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#3047ff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="REFRESH")
        self.button5.configure(command=self.delete_emp)"""


        self.button6 = Button(emp)
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

        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)
        self.tree = ttk.Treeview(emp)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=270)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=270)
        

        self.tree.configure(
            columns=(
                "Name",
                "Age",
                "Gender",
                "Mobile No.",
                "Email-Id",
                #"Previous History",
                #"Prescription" 
                ))

        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Age", text="Age", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)
        self.tree.heading("Mobile No.", text="Mobile No.", anchor=W)
        self.tree.heading("Email-Id", text="Email-Id", anchor=W)
        #self.tree.heading("Previous History", text="Previous History", anchor=W)
        #self.tree.heading("Prescription", text="Prescription", anchor=W)

        self.tree.column("#0", stretch=YES, minwidth=0, width=-75)
        self.tree.column("#1", stretch=YES, minwidth=0, width=90)
        self.tree.column("#2", stretch=YES, minwidth=0, width=10)
        self.tree.column("#3", stretch=YES, minwidth=0, width=30)
        self.tree.column("#4", stretch=YES, minwidth=0, width=85)
        self.tree.column("#5", stretch=YES, minwidth=0, width=100)
        #self.tree.column("#6", stretch=YES, minwidth=0, width=200)
        #self.tree.column("#7", stretch=YES, minwidth=0, width=80)

        self.DisplayData()
        #---------------------second part---------------------------------------------------#
        self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(emp, orient=VERTICAL)
        self.tree1 = ttk.Treeview(emp)
        self.tree1.place(relx=0.307, rely=0.573, width=880, height=270)
        self.tree1.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree1.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.573, width=22, height=270)
        self.scrollbarx.place(relx=0.307, rely=0.928, width=878, height=22)

        self.tree1.configure(
            columns=(
                "Name",
                "Age",
                "Gender",
                "Mobile No.",
                "Email-Id",
                #"Previous History",
                #"Prescription" 
                ))

        self.tree1.heading("Name", text="Name", anchor=W)
        self.tree1.heading("Age", text="Age", anchor=W)
        self.tree1.heading("Gender", text="Gender", anchor=W)
        self.tree1.heading("Mobile No.", text="Mobile No.", anchor=W)
        self.tree1.heading("Email-Id", text="Email-Id", anchor=W)
        #self.tree1.heading("Previous History", text="Previous History", anchor=W)
        #self.tree1.heading("Prescription", text="Prescription", anchor=W)

        self.tree1.column("#0", stretch=YES, minwidth=0, width=-75)
        self.tree1.column("#1", stretch=YES, minwidth=0, width=90)
        self.tree1.column("#2", stretch=YES, minwidth=0, width=10)
        self.tree1.column("#3", stretch=YES, minwidth=0, width=30)
        self.tree1.column("#4", stretch=YES, minwidth=0, width=85)
        self.tree1.column("#5", stretch=YES, minwidth=0, width=100)
        #self.tree1.column("#6", stretch=YES, minwidth=0, width=200)
        #self.tree1.column("#7", stretch=YES, minwidth=0, width=80)

        self.DisplayQueue()

    
        
    def DisplayQueue(self):
        global acc
        f=open("patientqueue.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree1.insert("", "end", values=(data))



    
        
    def DisplayData(self):
        global acc
        f=open("patientrecord.csv","r")
        a=csv.reader(f)
        acc=[]    
        
        for row in a:
            acc.append(row)

        for data in acc:
            self.tree.insert("", "end", values=(data))

    def search_emp(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)
            
        to_search = self.entry1.get()
        for search in val:
            if search==to_search:
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Account with Name: {} found.".format(self.entry1.get()), parent=self.emp)
                break
        else: 
              messagebox.showerror("Oops!!", "Account with Name: {} not found.".format(self.entry1.get()), parent=self.emp)
    
    sel = []
    def on_tree_select(self, Event):
        fl = open ("patientrecord.csv","r")
        self.sel.clear()
        for i in self.tree.selection():
            tr=(self.tree.item(i)["values"])
            if i not in self.sel:
                row = tr
                self.sel.append(row)
    
    def naturef(self):
            sure = messagebox.askyesno("Nature","Is visit urgent?", parent=self.emp) 
            return sure 

    def update_emp(self):
        if len(self.sel) == 1:
            
            truth = self.naturef()
            if truth == True:
                self._que.insert_first(self.sel[0])
                
            else:
                self._que.insert_last(self.sel[0])
               
            
            x = self._que.__str__()
            
            if len(x) > self._queuelimit:
                messagebox.showerror("Queue Full","Doctor Queue Full! \nPlease visit later")
            else:
                f = open("patientqueue.csv","w",newline="")
                a = csv.writer(f)
                a.writerows(x)
                f.close()
                messagebox.showinfo("Success!!","Patient successfully added to the queue")
                self.tree1.delete(*self.tree1.get_children())
                self.DisplayQueue()
        else:
            messagebox.showerror("Error","Please select a patient to add to queue.")     

    def add_emp(self):
        self.emp.destroy()
        global e_add
        e_add = Tk()
        page6 = add_employee(e_add)
        e_add.protocol("WM_DELETE_WINDOW", self.ex)
        e_add.mainloop()


    def ex(self):
        e_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()    


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.emp.destroy()

    """ def delete_emp(self):
       self.emp.destroy()
       page()
 """

class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Patient")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/addpat.png")
        self.label1.configure(image=self.img)


        self.r1 = e_add.register(self.testint)
        self.r2 = e_add.register(self.testchar)

        self.entry1 = Entry(e_add)
        self.entry1.place(relx=0.132, rely=0.296, width=453, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")


        self.entry2 = Entry(e_add)
        self.entry2.place(relx=0.132, rely=0.413, width=453, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_add)
        self.entry3.place(relx=0.132, rely=0.529, width=453, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")

        self.entry4 = Entry(e_add)
        self.entry4.place(relx=0.527, rely=0.296, width=453, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")

        self.entry5 = Entry(e_add)
        self.entry5.place(relx=0.527, rely=0.413, width=453, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(relx=0.527, rely=0.529, width=453, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")

        self.entry7 = Entry(e_add)
        self.entry7.place(relx=0.330, rely=0.683, width=453, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
        

        #=========== BACK ==================================================
        def backf():
            e_add.destroy()
            page()

        self.back_button_label = Button(e_add, text=">> Back <<", font=("yu gothic ui", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="black", activebackground="black", fg="white",command=backf)
        self.back_button_label.place(relx=0.39, rely=0.9, width=300, height=25)

        self.button1 = Button(e_add)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#3047ff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(e_add)
        self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#3047ff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#3047ff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)



    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False
    
    def add(self):
        ename = self.entry1.get()
        enum = self.entry2.get()
        eage = self.entry3.get()
        egender = self.entry4.get()
        eadd = self.entry5.get()
        eissue = self.entry6.get()
        epres = self.entry7.get()

        if ename.strip():
            if valid_phone(enum):
                if int(eage)<=125:
                    if egender== "Male" or " Female" or " M" or" F" or "m" or "f":
                        if "@" in eadd:
                                f=open("patientrecord.csv","a+",newline="")
                                data=[ename.title(),eage,egender,enum,eadd,eissue,epres]
                                cw=csv.writer(f)
                                cw.writerow(data)
                                f.close()
                                messagebox.showinfo("Success!!", "Patient successfully added in database.", parent=e_add)
                                self.clearr()
                        else:
                            messagebox.showerror("Oops!", "Please enter a proper email address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter the correct gender.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Please enter the correct age.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter the name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)

#==================================ADD TO QUEUE===================================================================

def page():
    emp = Tk()
    Employee(emp)
    emp.mainloop()

if __name__ == '__main__':
    page()
