from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import adminlogin,receplogin,doclogin, doctormain

class Invoice:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.title('Invoice')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('./images/invoice2.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=1366,height=768)
        
        amt=random.choice([375,400,425,450,475,500])
        self.entry1 = Label(self.window,text=str(amt))
        self.entry1.place(relx=0.56, rely=0.39)
        self.entry1.configure(font=("gotham", 42, "bold"),bg='black',fg='white')
        self.entry1.configure(relief="flat")

        self.entry2 = Entry(self.window)
        self.entry2.place(relx=0.45, rely=0.500,height=40,width=200)
        self.entry2.configure(font=("gotham", 13, "bold"),bg='white',fg='black')
        self.entry2.configure(relief="flat")
        
        l=[]
        def getamt():
            paid=self.entry2.get()
            if paid == '':
                messagebox.showwarning('#ErrorSB404', 'Please enter an amount')
            else:
                bal=int(paid)-int(amt)

                self.entry1 = Label(self.window,text=str(bal))
                self.entry1.place(relx=0.365, rely=0.5663)
                self.entry1.configure(font=("gotham", 42, "bold"),bg='black',fg='white')
                self.entry1.configure(relief="flat")
            
        
        self.done_button_label = Button(self.window, text="DONE", font=("yu gothic ui", 13, "bold"), bg='white', cursor="hand2",
                                          borderwidth=0, background="white", activebackground="black", fg="black",command=getamt)
        self.done_button_label.place(relx=0.62, rely=0.51, width=100, height=25)
        

        def exitf():
            self.window.destroy()
            doctormain.page()

        self.back_button_label = Button(self.window, text=">> BACK <<", font=("yu gothic ui", 13, "bold"), bg='black', cursor="hand2",
                                          borderwidth=0, background="black", activebackground="black", fg="white",command=exitf)
        self.back_button_label.place(relx=0.39, rely=0.91, width=300, height=25)
   
def page():
    window = Tk()
    Invoice(window)
    window.mainloop()


if __name__ == '__main__':
    page()

""" High,10,f,1237894560,high@,huigih ho,hjgkj ho
S,19,F,1234567890,@,q,t
Saranya,12,F,9999999999,@,cough,tablets
Boom,15,M,1234567890,@@,some,tabtab
Lala,90,M,4567891230,lala@,lala,lala
Sai,19,M,1234567890,sai@,none,none
Lol,19,M,4568712517,lala@,lolo,kiki
Sai,09,M,4566454551,@,@@@@,@@@@@@@@@ """
