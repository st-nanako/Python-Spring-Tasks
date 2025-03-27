import tkinter as tk
from tkinter import messagebox
from db import insert_user,get_account_by_email
from maile import code_mail,Register_mail


class LoCode(tk.Frame):
    def __init__(self, master,code,mail,name,pw,icon):#
        super().__init__(master,bg='#FFFFFF',width=400, height=400)
        self.pack()
        self.code = code
        self.mail = mail
        self.name = name
        self.pw = pw
        self.icon = icon
        master.geometry('400x400')
        master.title('確認コード入力画面')

        self.create_widgets()

    def create_widgets(self):
        self.label_login = tk.Label(self,text='確認コード入力',font=('',20),bg='#FFFFFF',fg='#8A2BE2')
        self.label_login.place(x=115,y=30)
        
        self.label_code = tk.Label(self,text='確認コード',bg='#FFFFFF')
        self.label_code.place(x=100,y=140)
        self.entry_code = tk.Entry(self,width=35,bg='#D8BFD8')
        self.entry_code.place(x=100,y=170)

        # self.label_pw = tk.Label(self,text='確認コード',bg='#FFFFFF')
        # self.label_pw.place(x=100,y=260)
        # self.entry_pw = tk.Entry(self,width=35,bg='#E0FFFF')
        # self.entry_pw.place(x=100,y=290)
        
        self.label_message = tk.Label(self,text='',bg='#FFFFFF')
        self.label_message.place(x=120,y=200)
        
        self.register_button = tk.Button(self,text='確定',width=20,bg='#1E90FF',fg='#FFFFFF',font=('',10,'bold'),command=self.code_event)
        self.register_button.place(x=120,y=230)
        self.return_button = tk.Button(self,text='戻る',width=20,bg='#FFFFFF',fg='#1E90FF',font=('',10,'bold'),command=self.return_event)
        self.return_button.place(x=120,y=270)
        
    def return_event(self):
        from register import Register
        self.destroy()
        Register(self.master)
        
    def code_event(self):
        print(self.code,self.entry_code.get(),type(self.code),type(self.entry_code.get()))
        entry_code = self.entry_code.get()
        if str(self.code) == entry_code:
            insert_user(self.name,self.mail,self.pw,self.icon)
            messagebox.showinfo('成功','登録に成功しました。')
            # Register_mail(self.mail,self.name)
            from login import Login
            self.destroy()
            Login(self.master)
        else:
            self.label_message.configure(text='確認コードが違います',bg='#FFFFFF',fg='red',font=('',13))
        
# if __name__ == '__main__':
#     root = tk.Tk()
#     app = RePassCode(master=root)
#     app.mainloop()