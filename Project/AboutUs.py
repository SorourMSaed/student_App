from tkinter import *

class about:
    def __init__(self) :
          self.close= Toplevel()
          self.close.geometry("250x150+600+250")
          self.close.config(background='pink')
          self.close.iconbitmap('photo//pink_windows_pink_folder_folder_icon_250634.ico')
          self.close.title("About")
          btn=Button(self.close,text="Back", width=10,height=1,command=self.lolo,bg='#EC7180')
          btn.place(x=85,y=110)
          lab=Label(self.close,text="|Thank you for using our App|\n Worked By: \n Eng.Sorour Masoud Saed \n Eng.Alaa Ismail Mahmoud\n",background='#EC7180')
          lab.place(x=40,y=20)

    def lolo(self):
           self.close.destroy()
           self.close.update()