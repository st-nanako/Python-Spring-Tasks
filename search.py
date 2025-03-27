import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
# from db import select_books,search_books

class Search(tk.Frame):
    def __init__(self, master):#,account
        super().__init__(master,width=850,height=600)
        # self.account = account
        self.pack()

        master.geometry('850x600')
        master.title('ユーザーの検索と一覧')

        self.create_widgets()


    def create_widgets(self):
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
        
        # ユーザー検索
        self.label_user_search = tk.Label(self,text='ユーザー検索',font=('',15))
        self.label_user_search.place(x=200,y=50)
        self.label_user_name = tk.Label(self,text='ユーザー名：')
        self.label_user_name.place(x=200,y=100)
        self.entry_usre_name = tk.Entry(self)
        self.entry_usre_name.place(x=270,y=100)
        self.entry_title_author = tk.Entry(self)
        self.entry_title_author.place()
        
        self.search_button = tk.Button(self,text='検索')#,command=self.search
        self.search_button.place()
        self.allbook_button = tk.Button(self,text='全て表示')#,command=self.all
        self.allbook_button.place()
        
        self.label_message = tk.Label(self,text='')
        self.label_message.place()
        
        # ユーザー表示エリア（スクロール対応）
        self.display_canvas = tk.Canvas(self, width=600, height=300)
        self.display_canvas.place(x=190, y=200)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.display_canvas.yview)#yview y軸のスクロールバー、orient スクロールバーの方向、vertical 縦方向に動かせるように設定
        self.scrollbar.place(x=790, y=200, height=300)

        self.display_canvas.configure(yscrollcommand=self.scrollbar.set)

        # ユーザーアイコンを配置する内部フレーム
        self.posts_frame = tk.Frame(self.display_canvas)
        self.display_canvas.create_window((0, 0), window=self.posts_frame, anchor="nw")

        self.posts_frame.bind("<Configure>", lambda e: self.display_canvas.configure(scrollregion=self.display_canvas.bbox("all")))
        
        # 文章検索
        # self.label_text_search = tk.Label(self,text='文章検索',font=('',15))
        # self.label_text_search.place(x=500,y=50)
        # self.label_title_author = tk.Label(self,text='文章：')
        # self.label_title_author.place(x=500,y=100)
        # self.entry_usre_name = tk.Entry(self)
        # self.entry_usre_name.place(x=550,y=100)
        # self.entry_title_author = tk.Entry(self)
        # self.entry_title_author.place()
        
        # self.search_button = tk.Button(self,text='検索')#,command=self.search
        # self.search_button.place()
        # self.allbook_button = tk.Button(self,text='全て表示')#,command=self.all
        # self.allbook_button.place()
        
        # self.label_message = tk.Label(self,text='')
        # self.label_message.place()
        
        # # Treeview
        # self.treeview = ttk.Treeview(self,show='headings',height=5)
        # self.treeview.pack()
        # # 列の名前を設定
        # header = ('id','name')
        # self.treeview.configure(columns=header)
        # # 列名の設定 
        # self.treeview.heading('id',text='ID')
        # self.treeview.heading('name',text='名前')
        
        # # 列幅の設定
        # self.treeview.column('id',width=30,anchor=tk.CENTER)
        # self.treeview.column('name',width=150,anchor=tk.CENTER)
        
        # データの挿入
        # rows = select_books()
        # for row in rows:
        #     self.treeview.insert('',index='end',values=row)
        
        # self.return_button = tk.Button(self,text='戻る',command=self.return_event)
        # self.return_button.pack()
        
    # def return_event(self):
    #     if self.account[3] == 1:    
    #         from menu_user import User
    #         self.destroy()
    #         User(self.master,self.account)
    #     else:
    #         from menu_admin import Admin
    #         self.destroy()
    #         Admin(self.master,self.account)
            
    # def all_book(self):
    #     for i in self.treeview.get_children():
    #             self.treeview.delete(i)
    #     rows = select_books()   
    #     for row in rows:
    #         self.treeview.insert('',index='end',values=row)
    
    # def search_book(self):
    #     word = self.entry_title_author.get()
        
    #     if not word:
    #         self.label_message.configure(text='入力がありません',fg='red',font=('',13))
    #     else:
    #         for i in self.treeview.get_children():
    #             self.treeview.delete(i)
    #         rows = search_books(word)
    #         if len(rows) == 0:
    #             self.label_message.configure(text='一致するものがありません。',fg='red',font=('',13))
    #         else:    
    #             for row in rows:
    #                 self.treeview.insert('',index='end',values=row)
                    
if __name__ == '__main__':
    root = tk.Tk()
    app = Search(master=root)
    app.mainloop()