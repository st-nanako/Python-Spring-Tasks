import tkinter as tk
from PIL import Image, ImageTk


class User(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=850, height=600)
        self.pack()

        master.geometry('850x600')
        master.title('ホーム画面')

        self.create_widgets()

    def create_widgets(self):
        # 投稿リスト
        self.post_text_list = []
        # テキスト入力ボックス
        self.post_text = tk.Text(self, width=66, height=10)
        self.post_text.place(x=190, y=20)

        # ポストボタン
        self.post_button = tk.Button(
            self, text='ポスト', width=10, bg='#6A5ACD', fg='#FFFFFF',
            font=('', 10, 'bold'), command=self.post_message
        )
        self.post_button.place(x=660, y=125)

        # 投稿表示エリア（スクロール対応）
        self.display_canvas = tk.Canvas(self, width=600, height=300)
        self.display_canvas.place(x=190, y=200)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.display_canvas.yview)#yview y軸のスクロールバー、orient スクロールバーの方向、vertical 縦方向に動かせるように設定
        self.scrollbar.place(x=790, y=200, height=300)

        self.display_canvas.configure(yscrollcommand=self.scrollbar.set)

        # 投稿を配置する内部フレーム
        self.posts_frame = tk.Frame(self.display_canvas)
        self.display_canvas.create_window((0, 0), window=self.posts_frame, anchor="nw")

        self.posts_frame.bind("<Configure>", lambda e: self.display_canvas.configure(scrollregion=self.display_canvas.bbox("all")))
        

    def post_message(self):
        # テキストボックスから内容を取得
        content = self.post_text.get("1.0", "end").strip()
        if content:  # 空白以外なら処理
            self.post_text_list.insert(0,content)
            
            # 投稿フレームをリセット
            for widget in self.posts_frame.winfo_children():  # posts_frame内の全てのウィジェットを取得
                widget.destroy()  # 各ウィジェットを削除
                
            for text in self.post_text_list:
                # 投稿フレームを作成
                post_frame = tk.Frame(self.posts_frame, bg="#f0f0f0", pady=5)
                post_frame.pack(fill="x", pady=5)

                # アイコン画像の読み込みと表示
                user_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/初期画像user.png").resize((50, 50))  # サイズを調整
                user_icon = ImageTk.PhotoImage(user_img)

                icon_label = tk.Label(post_frame, image=user_icon)
                icon_label.image = user_icon  # 参照を保持
                icon_label.pack(side="left", padx=5)

                heart_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/ハート(なし).png").resize((30, 30))  # サイズを調整
                heart_icon = ImageTk.PhotoImage(heart_img)
                
                self.heart_label = tk.Label(post_frame, image=heart_icon)
                self.heart_label.image = heart_icon  # 参照を保持
                self.heart_label.pack(side="right", padx=5)
                
                # ステータス設定
                # self.heart_status = False
                
                self.heart_label.heart_status = False
                
                self.heart_label.bind("<Button-1>",self.heart_label_click)

                # 投稿テキストのラベルを作成
                text_label = tk.Label(post_frame, text=text, wraplength=400, justify="left", anchor="w", bg="#ffffff", padx=10)
                text_label.pack(side="left", fill="x", expand=True)

                
            

            # テキストボックスをクリア
            self.post_text.delete("1.0", "end")
    
    def heart_label_click(self,event):
        if event.widget.heart_status:
            heart_false_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/ハート(なし).png").resize((30, 30))  # サイズを調整
            heart_false_icon = ImageTk.PhotoImage(heart_false_img)
            event.widget.configure(image=heart_false_icon)
            event.widget.image = heart_false_icon  # 参照を保持
            event.widget.heart_status = False
        else:
            heart_true_img = Image.open("C:/Users/satou/Desktop/春休み課題/Python-Spring-Tasks/img/ハート(あり).png").resize((30, 30))  # サイズを調整
            heart_true_icon = ImageTk.PhotoImage(heart_true_img)
            event.widget.configure(image=heart_true_icon)
            event.widget.image = heart_true_icon  # 参照を保持
            event.widget.heart_status = True

if __name__ == "__main__":
    root = tk.Tk()
    app = User(root)
    app.mainloop()
