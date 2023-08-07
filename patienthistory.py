from tkinter import *
from PIL import ImageTk, Image
import doctormain

class Patient_page:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.title('Patient History')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('./images/viewpatient.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.place(width=1366,height=768)


        def exitf():
            self.window.destroy()
            doctormain.page()

        self.back_button_label = Button(self.window, text='BACK', font=("gotham", 13, "bold"), width=22, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=exitf)
        self.back_button_label.place(relx=0.406, rely=0.833, width=260, height=37)

        self.label = Label(self.window, text='Name: ', font=("gotham", 13, "bold"), width=22,bg='black',fg='white')
        self.label.place(relx=0.1, rely=0.1, width=260, height=37)

def page():
    window = Tk()
    Patient_page(window)
    window.mainloop()

if __name__ == '__main__':
    page() 


