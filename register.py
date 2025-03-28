import tkinter as tk
from tkinter import messagebox
import random
from tkinter import filedialog
from PIL import Image,ImageTk
from db import get_account_by_email
from maile import code_mail


class Register(tk.Frame):
    def __init__(self, master):
        super().__init__(master,width=550, height=550,bg='#FFFFFF')
        self.pack()

        master.geometry('550x550')
        master.title('新規登録')

        self.create_widgets()

    def create_widgets(self):
        self.label_login = tk.Label(self,text='新規登録',font=('',20),fg='#8A2BE2',bg='#FFFFFF')
        self.label_login.place(x=215,y=30)
        
        self.label_name = tk.Label(self,text='ユーザー名',bg='#FFFFFF')
        self.label_name.place(x=50,y=140)
        self.entry_name = tk.Entry(self,width=35,bg='#D8BFD8')
        self.entry_name.place(x=50,y=170)
        
        self.label_mail = tk.Label(self,text='メールアドレス',bg='#FFFFFF')
        self.label_mail.place(x=50,y=200)
        self.entry_mail = tk.Entry(self,width=35,bg='#D8BFD8')
        self.entry_mail.place(x=50,y=230)

        self.label_pw = tk.Label(self,text='パスワード',bg='#FFFFFF')
        self.label_pw.place(x=50,y=260)
        self.entry_pw = tk.Entry(self,width=35,bg='#D8BFD8',show='●')
        self.entry_pw.place(x=50,y=290)

        self.label_re_pw = tk.Label(self,text='パスワード確認',bg='#FFFFFF')
        self.label_re_pw.place(x=50,y=320)
        self.entry_re_pw = tk.Entry(self,width=35,bg='#D8BFD8',show='●')
        self.entry_re_pw.place(x=50,y=350)
        
        self.label_message = tk.Label(self,text='',bg='#FFFFFF')
        
        self.label = tk.Label(self,text='ユーザー画像を選択してください',bg='#FFFFFF')
        self.file_open_button = tk.Button(self,text='ファイルを開く',command=self.file_open)
        self.file_reset_button = tk.Button(self,text='選択を解除',command=self.file_reset)
        
        initial_user_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/初期画像user.png")
        self.initial_user_icon_img = ImageTk.PhotoImage(initial_user_img)
        self.user_icon = tk.Label(self,image=self.initial_user_icon_img)
        self.user_icon.place(x=350,y=170)
        self.icon_status = False
        self.file_name = ''
        
        self.label.place(x=350,y=140)
        self.file_open_button.place(x=350,y=350)
        self.file_reset_button.place(x=450,y=350)
        
        self.register_button = tk.Button(self,text='新規登録',width=20,bg='#8A2BE2',fg='#FFFFFF',font=('',10,'bold'),command=self.register_user)#
        self.register_button.place(x=190,y=430)
        self.return_button = tk.Button(self,text='戻る',width=20,bg='#FFFFFF',fg='#8A2BE2',font=('',10,'bold'),command=self.return_event)#
        self.return_button.place(x=190,y=470)

    
    def file_reset(self):
        self.user_icon.configure(image=self.initial_user_icon_img)
        self.icon_status = False
    
    def file_open(self):
        file_type = [('画像ファイル','*.jpg;*.gif;*.png')]
        
        self.file_name = filedialog.askopenfilename(filetypes=file_type)
        if self.file_name == '':
            pass
        else:
            img = Image.open(self.file_name)
            img = img.resize((135,135))
            self.user_photo_img = ImageTk.PhotoImage(img)
            self.user_icon.configure(image=self.user_photo_img)
            self.icon_status = True
        
    def return_event(self):
        from login import Login
        self.destroy()
        Login(self.master)
        
    def register_user(self):
        if not self.entry_name.get() or not self.entry_mail.get() or not self.entry_pw.get():
            self.label_message.configure(text='',bg='#FFFFFF')
            self.entry_name.configure(bg='#D8BFD8')
            self.entry_mail.configure(bg='#D8BFD8')
            self.entry_pw.configure(bg='#D8BFD8')
            self.entry_re_pw.configure(bg='#D8BFD8')
            entrys_get = [self.entry_name.get(),self.entry_mail.get(),self.entry_pw.get(),self.entry_re_pw.get()]
            for i,entry in enumerate(entrys_get):
                if not entry:
                    if i == 0:
                        self.entry_name.configure(bg='#FFC0CB')
                    elif i == 1:
                        self.entry_mail.configure(bg='#FFC0CB')
                    elif i == 2:
                        self.entry_pw.configure(bg='#FFC0CB')
                    elif i == 3:
                        self.entry_re_pw.configure(bg='#FFC0CB')

            self.label_message.configure(text='入力されていない項目があります',bg='#FFFFFF',fg='red',font=('',13))
            self.label_message.place(x=90,y=390)

        elif len(self.entry_pw.get()) < 8:
            self.label_message.configure(text='パスワードは8文字以上です',bg='#FFFFFF',fg='red',font=('',13))
            self.label_message.place(x=90,y=390)
            
        elif self.entry_pw.get() != self.entry_re_pw.get():
            self.entry_re_pw.configure(bg='#FFC0CB')
            self.label_message.configure(text='確認パスワードが間違っています',bg='#FFFFFF',fg='red',font=('',13))
            self.label_message.place(x=90,y=390)
        
            
        elif get_account_by_email(self.entry_mail.get()) is None:
            import re

            # メールアドレスのフォーマットをチェック
            def check_email_format(email):
                email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                return re.match(email_regex, email) is not None

            # メールアドレスの検証関数
            def validate_email(email):
                if check_email_format(email):
                    return True
                else:
                    return False
                    
            if validate_email(self.entry_mail.get()):
                code = random.randint(100000, 999999)
                mail = self.entry_mail.get()
                name = self.entry_name.get()
                pw = self.entry_pw.get()
                if self.icon_status:
                    self.file_path = self.file_name
                else:
                    self.file_path = "C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/初期画像user.png"
                icon = self.file_path
                print(icon)
                print(code)
                # code_mail(mail,code)
                messagebox.showinfo('確認コード','確認コードを送信しました。')
                from login_code import LoCode
                self.destroy()
                LoCode(self.master,code,mail,name,pw,icon)
                
                # self.entry_mail.delete(0,tk.END)
                # self.entry_name.delete(0,tk.END)
                # self.entry_pw.delete(0,tk.END)
                # self.entry_re_pw.delete(0,tk.END)
                # self.radio_status.set(0)
                # self.label_message.configure(text='',bg='#FFFFFF')
                # self.entry_name.configure(bg='#E0FFFF')
                # self.entry_mail.configure(bg='#E0FFFF')
                # self.entry_pw.configure(bg='#E0FFFF')
                # self.entry_re_pw.configure(bg='#E0FFFF')
            else:
                self.entry_mail.configure(bg='#FFC0CB')
                self.label_message.configure(text='不正なメールアドレスです',bg='#FFFFFF',fg='red',font=('',13))
                self.label_message.place(x=90,y=390)
        else:
            self.label_message.configure(text='既にそのメールは登録されています。',bg='#FFFFFF',fg='red',font=('',13))
            self.label_message.place(x=90,y=390)
            self.entry_mail.configure(bg='#FFC0CB')
            
    
if __name__ == '__main__':
    root = tk.Tk()
    app = Register(master=root)
    app.mainloop()