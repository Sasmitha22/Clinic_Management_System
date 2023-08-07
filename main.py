from tkinter import *
from PIL import ImageTk, Image
import adminlogin,receplogin,doclogin

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('./images/main.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=1366,height=768)

         # ========================================================================
        # ============================admin button================================
        # ========================================================================
        def adminf():
            self.window.destroy()
            adminlogin.page()
    

        self.admin = Button(self.window, text='ADMIN', font=("gotham", 13, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=adminf)
        self.admin.place(relx=0.58, rely=0.45)

         # ========================================================================
        # ============================doc button================================
        # ========================================================================

        def docf():
            self.window.destroy()
            doclogin.page()
            
        self.doc = Button(self.window, text='DOCTOR', font=("gotham", 13, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=docf)
        self.doc.place(relx=0.58, rely=0.55)

        
        # ========================================================================
        # ============================recep button================================
        # ========================================================================

        def recepf():
            self.window.destroy()
            receplogin.page()

        self.recep = Button(self.window, text='RECEPTIONIST', font=("gotham", 13, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=recepf)
        self.recep.place(relx=0.58, rely=0.645)

        #=========== EXIT ==================================================
        def exitf():
            self.window.destroy()

        self.back_button_label = Button(self.window, text=">> Exit <<", font=("yu gothic ui", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="black", fg="white",command=exitf)
        self.back_button_label.place(relx=0.565, rely=0.72, width=300, height=25)
   
def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
