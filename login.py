import tkinter as tk
from PIL import Image,ImageTk
from db import login
from home import Home

class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg='#FFFFFF',width=400, height=500)
        self.pack()

        master.geometry('400x500')
        master.title('ログイン')

        self.create_widgets()

    def create_widgets(self):
        img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/sns_icon.png")
        self.icon_img = ImageTk.PhotoImage(img)
        self.label_icon = tk.Label(self,image=self.icon_img)
        self.label_icon.place(x=145,y=10)
        
        self.label_mail = tk.Label(self,text='メールアドレス',bg='#FFFFFF')
        self.label_mail.place(x=100,y=180)
        self.entry_mail = tk.Entry(self,width=35,bg='#DDA0DD')
        self.entry_mail.place(x=100,y=210)

        self.label_pw = tk.Label(self,text='パスワード',bg='#FFFFFF')
        self.label_pw.place(x=100,y=240)
        self.entry_pw = tk.Entry(self,width=35,bg='#DDA0DD',show='●')
        self.entry_pw.place(x=100,y=270)

        self.label_reset_pw = tk.Label(self,text='パスワードを忘れた場合',font=('',10,'normal','roman','underline'),fg='#9400D3',bg='#FFFFFF')
        self.label_reset_pw.place(x=180,y=290)
        
        self.label_message = tk.Label(self,text='',bg='#FFFFFF')
        
        self.login_button = tk.Button(self,text='ログイン',width=20,bg='#8A2BE2',fg='#FFFFFF',font=('',10,'bold'),command=self.login_user)#
        self.login_button.place(x=120,y=380)
        self.register_button = tk.Button(self,text='新規登録',width=20,bg='#FFFFFF',fg='#8A2BE2',font=('',10,'bold'),command=self.register_user)#
        self.register_button.place(x=120,y=420)
        
        # イベントの割り当て
        self.label_reset_pw.bind('<Enter>',self.enter_event)
        self.label_reset_pw.bind('<Leave>',self.leave_event)
        self.label_reset_pw.bind('<Button-1>',self.click_event)
    
    # reset_pwのイベント
    def enter_event(self,event):
        self.label_reset_pw.configure(fg='#EE82EE')
    def leave_event(self,event):
        self.label_reset_pw.configure(fg='#9400D3')
    def click_event(self,event):
        from re_pass_mail import RePassMail
        self.destroy()
        RePassMail(self.master)
        
    def register_user(self):
        from register import Register
        self.destroy()
        Register(self.master)

        
    # ログイン処理
    def login_user(self):
        if not self.entry_mail.get() or not self.entry_pw.get():
            self.label_message.configure(text='入力されていない項目があります',bg='#FFFFFF',fg='red',font=('',13))
            self.label_message.place(x=80,y=325)
        else:
            mail = self.entry_mail.get()
            pw = self.entry_pw.get()
            account = login(mail,pw)
            if account is None:
                self.label_message.configure(text='ログインに失敗しました\n再度パスワードとメールアドレスを確認してください',bg='#FFFFFF',fg='red',font=('',13))
                self.label_message.place(x=23,y=325)
            else:
                self.destroy()
                Home(self.master,account)#

# 利用者
# yuuki5.emerald@gmail.com
# 55555555
# kila10680@gmail.com
# 88888888
# 管理者
# n.sato.sys24@morijyobi.ac.jp
# 11111111

if __name__ == '__main__':
    root = tk.Tk()
    app = Login(master=root)
    app.mainloop()