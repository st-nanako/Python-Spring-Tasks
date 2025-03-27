import tkinter as tk
from PIL import Image,ImageTk

def menu_icon():
    # アイコン生成
        home_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/homeアイコン.png")
        self.home_icon_img = ImageTk.PhotoImage(home_img)
        self.home_icon = tk.Label(self,image=self.home_icon_img)
        self.home_icon.place(x=15,y=10)
        self.label_home = tk.Label(self,text='ホーム')
        self.label_home.place(x=65,y=140)
        
        search_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/検索アイコン.png")
        self.search_icon_img = ImageTk.PhotoImage(search_img)
        self.search_icon = tk.Label(self,image=self.search_icon_img)
        self.search_icon.place(x=15,y=180)
        self.label_search = tk.Label(self,text='検索')
        self.label_search.place(x=65,y=290)

        user_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/初期画像user.png")
        self.user_icon_img = ImageTk.PhotoImage(user_img)
        self.user_icon = tk.Label(self,image=self.user_icon_img)
        self.user_icon.place(x=15,y=350)
        self.label_user = tk.Label(self,text='ユーザー名')
        self.label_user.place(x=60,y=510)