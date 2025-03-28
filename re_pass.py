import tkinter as tk
# from tkinter import messagebox
from db import re_pass
# from maile import code_mail

class RePass(tk.Frame):
    def __init__(self, master,mail):#
        super().__init__(master,bg='#FFFFFF',width=400, height=500)
        self.pack()
        self.mail = mail
        master.geometry('400x500')
        master.title('パスワード再設定')

        self.create_widgets()

    def create_widgets(self):
        self.label_login = tk.Label(self,text='パスワード再設定',font=('',20),bg='#FFFFFF',fg='#8A2BE2')
        self.label_login.place(x=110,y=30)
        
        self.label_pw = tk.Label(self,text='パスワード',bg='#FFFFFF')
        self.label_pw.place(x=100,y=100)
        self.entry_pw = tk.Entry(self,width=35,bg='#D8BFD8',show='●')
        self.entry_pw.place(x=100,y=130)

        self.label_re_pw = tk.Label(self,text='パスワード確認',bg='#FFFFFF')
        self.label_re_pw.place(x=100,y=160)
        self.entry_re_pw = tk.Entry(self,width=35,bg='#D8BFD8',show='●')
        self.entry_re_pw.place(x=100,y=190)
        
        self.label_message = tk.Label(self,text='',bg='#FFFFFF')
        self.label_message.place(x=100,y=250)
        
        self.register_button = tk.Button(self,text='確定',width=20,bg='#1E90FF',fg='#FFFFFF',font=('',10,'bold'),command=self.code)
        self.register_button.place(x=120,y=300)
        
    def code(self):
        if self.entry_pw.get() == self.entry_re_pw.get() and len(self.entry_pw.get()) >= 8:
            re_pass(self.mail,self.entry_pw.get())
            from login import Login
            self.destroy()
            Login(self.master)
        elif len(self.entry_pw.get()) < 8:
            self.label_message.configure(text='パスワードは8文字以上です',bg='#FFFFFF',fg='red',font=('',13))
        else:
            self.label_message.configure(text='確認パスワードが違います')
        
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = RePass(master=root)
#     app.mainloop()