import tkinter as tk
from tkinter import messagebox
from db import get_account_by_email
from maile import code_mail
import random


class RePassMail(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg='#FFFFFF',width=400, height=500)
        self.pack()

        master.geometry('400x400')
        master.title('確認コード送信')

        self.create_widgets()

    def create_widgets(self):
        self.label_login = tk.Label(self,text='確認コード送信',font=('',20),bg='#FFFFFF',fg='#8A2BE2')
        self.label_login.place(x=110,y=30)
        
        self.label_mail = tk.Label(self,text='メールアドレス',bg='#FFFFFF')
        self.label_mail.place(x=100,y=140)
        self.entry_mail = tk.Entry(self,width=35,bg='#D8BFD8')
        self.entry_mail.place(x=100,y=170)
        
        self.label_message = tk.Label(self,text='',bg='#FFFFFF')
        self.label_message.place(x=100,y=200)
        
        self.register_button = tk.Button(self,text='確認コードを送信',width=20,bg='#8A2BE2',fg='#FFFFFF',font=('',10,'bold'),command=self.code)
        self.register_button.place(x=120,y=230)
        self.return_button = tk.Button(self,text='戻る',width=20,bg='#FFFFFF',fg='#8A2BE2',font=('',10,'bold'),command=self.return_event)
        self.return_button.place(x=120,y=270)
        
    def return_event(self):
        from login import Login
        self.destroy()
        Login(self.master)
    
    def code(self):
        if not self.entry_mail.get():
            self.label_message.configure(text='入力して下さい',bg='#FFFFFF',fg='red',font=('',13))
        else:
            if get_account_by_email(self.entry_mail.get()) is None:
                self.label_message.configure(text='そのメールアドレスは登録されていません',bg='#FFFFFF',fg='red',font=('',13))
            else:
                code = random.randint(100000, 999999)
                mail = self.entry_mail.get()
                code_mail(mail,code)
                messagebox.showinfo('確認コード','確認コードを送信しました。')
                from re_pass_code import RePassCode
                self.destroy()
                RePassCode(self.master,code,mail)
            
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = RePassMail(master=root)
#     app.mainloop()