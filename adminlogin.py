from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import main,csv,adminmain

class LoginPage:
    def show(self):
        self.hide_button = Button(self.window, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(relx=0.795, rely=0.655)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(relx=0.795, rely=0.655)
        self.password_entry.config(show='*')

        
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.title('Admin Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('./images/adminlogin.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=1366,height=768)

        self.username_entry = Entry(self.window, relief="flat", bg="white", fg="black",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(relx=0.567, rely=0.539, width=300)
        self.username_entry.configure(relief="flat")
        
          # ========================================================================
        # ============================password====================================
        # ========================================================================

        self.password_entry = Entry(self.window, relief="flat", bg="white", fg="black",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(relx=0.567, rely=0.6437, width=300)
        self.password_entry.configure(relief="flat")
        
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        def adminf():
            self.window.destroy()
            adminmain.page()
            
        def signinf():
            flag=0
            uncheck=self.username_entry.get()
            pwdcheck=self.password_entry.get()
            with open("USER DATA FA.csv",'r') as f :
                data=list(csv.reader(f))
                for i in range(len(data)-1):
                    if data[i][2]==uncheck and data[i][3]==pwdcheck and data[i][1].lower()=="admin":
                        flag=1
                        messagebox.showinfo('#SuccessSB404', 'Login Successful!')
                        adminf()
                        break
                    
                if flag==0:
                    messagebox.showwarning('#ErrorSB404', 'Account Type/Username/Password Incorrect')

        
        self.login = Button(self.window, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=signinf)
        self.login.place(relx=0.578, rely=0.71)
        
        #=========== BACK ==================================================
        def backf():
            self.window.destroy()
            main.page()

        self.back_button_label = Button(self.window, text="Back <<", font=("yu gothic ui", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="black", activebackground="black", fg="white",command=backf)
        self.back_button_label.place(relx=0.57, rely=0.79, width=300, height=25)


        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='./images/show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='./images/hide.png')

        self.show_button = Button(self.window, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(relx=0.795, rely=0.655)

        # ===========================================================================================

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
