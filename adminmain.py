import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
import csv
import main

def valid_phone(phn):
    if phn.isdigit() and len(phn)==10:
        return True
    return False

def valid_pwd(pwd):
    if len(pwd)>8:
        return True
    return False

class Employee:
    def __init__(self, emp):
        
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
        emp.title("Employee Management")

        
        self.label1 = Label(emp)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/testemployee.png")
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
        self.button3.configure(text="""ADD ACCOUNT""")
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
        self.button4.configure(text="""UPDATE ACCOUNT""")
        self.button4.configure(command=self.update_emp)

        self.button5 = Button(emp)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#3047ff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#3047ff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE ACCOUNT""")
        self.button5.configure(command=self.delete_emp)

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
        self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.307, rely=0.924, width=878, height=22)

        self.tree.configure(
            columns=(
                "Name",
                "Account Type",
                "Username",
                "Password",
                "Phone No.",
                "Email-Id",
                "Gender" ))

        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Account Type", text="Account Type", anchor=W)
        self.tree.heading("Username", text="Username", anchor=W)
        self.tree.heading("Password", text="Password", anchor=W)
        self.tree.heading("Phone No.", text="Phone No.", anchor=W)
        self.tree.heading("Email-Id", text="Email-Id", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)

        self.tree.column("#0", stretch=YES, minwidth=0, width=0)
        self.tree.column("#1", stretch=YES, minwidth=0, width=80)
        self.tree.column("#2", stretch=YES, minwidth=0, width=90)
        self.tree.column("#3", stretch=YES, minwidth=0, width=100)
        self.tree.column("#4", stretch=YES, minwidth=0, width=80)
        self.tree.column("#5", stretch=YES, minwidth=0, width=80)
        self.tree.column("#6", stretch=YES, minwidth=0, width=200)
        self.tree.column("#7", stretch=YES, minwidth=0, width=80)

        self.DisplayData()

    
        
    def DisplayData(self):
        global acc
        f=open("USER DATA FA.csv","r")
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
                print("found")
                print(val[val.index(search)-1])
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Account with Name: {} found.".format(self.entry1.get()), parent=self.emp)
                break
        else: 
            messagebox.showerror("Oops!!", "Account with Name: {} not found.".format(self.entry1.get()), parent=self.emp)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_emp(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected employee(s)?", parent=self.emp)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)

                for j in range(len(val)):
                    if j%7==0:
                        to_delete.append(val[j])
                
                f=open("USER DATA FA.csv","r")
                a=csv.reader(f)
                acc=[]    
        
                for row in a:
                    acc.append(row)
                
                for r in range(len(to_delete)):
                    for r2 in range(len(acc)):
                        if str(to_delete[r])==str(acc[r2][0]):
                            del acc[r2]
                            break

                f=open("USER DATA FA.csv","w",newline="")
                a=csv.writer(f)
                a.writerows(acc)
                f.close()
                
                messagebox.showinfo("Success!!", "Account(s) deleted from database.", parent=self.emp)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
                                  
        else:
            messagebox.showerror("Error!!","Please select an employee.", parent=self.emp)

    def update_emp(self):
        global vall
        vall = []
        for i in self.sel:
            for j in self.tree.item(i)["values"]:
                vall.append(j)
        
        if len(self.sel)==1:
            self.emp.destroy()
            global e_update
            e_update = Tk()
            page8 = Update_Employee(e_update)
            
            e_update.protocol("WM_DELETE_WINDOW", self.ex2)
                    
            page8.entry1.insert(0, vall[0])
            page8.entry2.insert(0, vall[4])
            page8.entry3.insert(0, vall[2])
            #page8.entry4.insert(0, vall[1])
            page8.entry5.insert(0, vall[5])
            page8.entry6.insert(0, vall[3])
            page8.entry7.insert(0, vall[6])
            e_update.mainloop()
            
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select an employee to update.")
        else:
            messagebox.showerror("Error","Can only update one employee at a time.")

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

    def ex2(self):
        e_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            self.emp.destroy()
            



class add_employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Add Employee")

        self.label1 = Label(e_add)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/addacc2.png")
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

        self.entry4 = StringVar(e_add)
        self.entry4.set("Admin") # default value

        self.w = OptionMenu(e_add, self.entry4, "Admin","Doctor","Receptionist")
        self.w.place(relx=0.527, rely=0.296, width=453, height=30)

        """  self.entry4 = Entry(e_add)
        self.entry4.place(relx=0.527, rely=0.296, width=453, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P")) """

        self.entry5 = Entry(e_add)
        self.entry5.place(relx=0.527, rely=0.413, width=453, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_add)
        self.entry6.place(relx=0.527, rely=0.529, width=453, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

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
        self.button1.configure(font="-family { Poppins SemiBold} -size 14")
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
        eun = self.entry3.get()
        eacctype = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        egen=self.entry7.get()

        if ename.strip():
            if valid_phone(enum):
                if eun:
                    if eacctype:
                        if "@" in eadd:
                            if valid_pwd(epass):
                                f=open("USER DATA FA.csv","a+",newline="")
                                data=[ename.title(),eacctype.title(),eun,epass,enum,eadd,egen]
                                cw=csv.writer(f)
                                cw.writerow(data)
                                f.close()
                                messagebox.showinfo("Success!!", "Account successfully added in database.", parent=e_add)
                                self.clearr()
                            else:
                                messagebox.showerror("Oops!", "Please enter a proper password more than 8 characters.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter a proper email address.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter Account Type.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Please enter username.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
        else:
            messagebox.showerror("Oops!", "Please enter the name.", parent=e_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        #self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)


class Update_Employee:
    def __init__(self, top=None):
        top.geometry("1366x768")
        top.resizable(0, 0)
        top.title("Update Employee")

        self.label1 = Label(e_update)
        self.label1.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/updateacc2.png")
        self.label1.configure(image=self.img)

        self.r1 = e_update.register(self.testint)
        self.r2 = e_update.register(self.testchar)

        self.entry1 = Entry(e_update)
        self.entry1.place(relx=0.132, rely=0.296, width=453, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        
        self.entry2 = Entry(e_update)
        self.entry2.place(relx=0.132, rely=0.413, width=453, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

        self.entry3 = Entry(e_update)
        self.entry3.place(relx=0.132, rely=0.529, width=453, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")

        self.entry4 = StringVar(e_update)
        self.entry4.set("Admin") # default value

        self.w = OptionMenu(e_update, self.entry4, "Admin","Doctor","Receptionist")
        self.w.place(relx=0.527, rely=0.296, width=453, height=30)

        """ self.entry4 = Entry(e_update)
        self.entry4.place(relx=0.527, rely=0.296, width=453, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")
        self.entry4.configure(validate="key", validatecommand=(self.r2, "%P")) """

        self.entry5 = Entry(e_update)
        self.entry5.place(relx=0.527, rely=0.413, width=453, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.entry6 = Entry(e_update)
        self.entry6.place(relx=0.527, rely=0.529, width=453, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(show="*")

        self.entry7 = Entry(e_update)
        self.entry7.place(relx=0.330, rely=0.683, width=453, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")

        def backf():
            e_update.destroy()
            page()

        self.back_button_label = Button(e_update, text=">> Back <<", font=("yu gothic ui", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="black", activebackground="black", fg="white",command=backf)
        self.back_button_label.place(relx=0.39, rely=0.9, width=300, height=25)
        
        self.button1 = Button(e_update)
        self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#3047ff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#3047ff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(e_update)
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

    def update(self):
        ename = self.entry1.get()
        enum = self.entry2.get()
        eun = self.entry3.get()
        eacctype = self.entry4.get()
        eadd = self.entry5.get()
        epass = self.entry6.get()
        egen = self.entry7.get()

        if ename.strip():
            if valid_phone(enum):
                if eun:
                    if eacctype:
                        if "@" in eadd:
                            if valid_pwd(epass):
                                
                                f=open("USER DATA FA.csv","r")
                                a=csv.reader(f)
                                acc=[]    
        
                                for row in a:
                                    acc.append(row)
                                
                                for r in range(len(acc)):
                                    if str(vall[2])==str(acc[r][2]) and str(vall[3])==str(acc[r][3]):
                                        data=[ename.title(),eacctype.title(),eun,epass,enum,eadd,egen]
                                        acc[r]=data
                                        break
                            
                                f=open("USER DATA FA.csv","w",newline="")
                                a=csv.writer(f)
                                a.writerows(acc)
                                f.close()

                                messagebox.showinfo("Success!!", "Account successfully updated in database.", parent=e_update)
                                self.clearr()

                            else:
                                messagebox.showerror("Oops!", "Please enter a proper password more than 8 characters.", parent=e_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter a proper email address.", parent=e_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter Account Type.", parent=e_update)
                else:
                    messagebox.showerror("Oops!", "Please enter username.", parent=e_update)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=e_update)
        else:
            messagebox.showerror("Oops!", "Please enter the name.", parent=e_update)
        


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        #self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)

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

    
def page():
    emp = Tk()
    Employee(emp)
    emp.mainloop()

if __name__ == '__main__':
    page()
