import tkinter as tk
from PIL import Image, ImageTk

class User(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=800, height=600)
        self.pack()

        master.geometry('800x600')
        master.title('ホーム画面')

        self.create_widgets()

    def create_widgets(self):
        # アイコン生成（例として簡略化）
        self.label_home = tk.Label(self, text='ホーム')
        self.label_home.place(x=65, y=140)

        self.label_search = tk.Label(self, text='検索')
        self.label_search.place(x=65, y=290)

        self.label_user = tk.Label(self, text='ユーザー名')
        self.label_user.place(x=60, y=510)

        # テキスト入力ボックス
        self.post_text = tk.Text(self, width=60, height=10)
        self.post_text.place(x=190, y=20)

        # ポストボタン
        self.post_button = tk.Button(
            self, text='ポスト', width=10, bg='#6A5ACD', fg='#FFFFFF',
            font=('', 10, 'bold'), command=self.post_message
        )
        self.post_button.place(x=650, y=125)

        # 投稿表示エリア（例としてFrameを使用）
        self.display_frame = tk.Frame(self, width=500, height=300,bg='#FFFFFF')
        self.display_frame.place(x=190, y=200)
        self.display_frame.pack_propagate(False)

        self.display_texts = []

    def post_message(self):
        # テキストボックスから入力された内容を取得
        content = self.post_text.get("1.0", "end").strip()
        if content:  # 空でない場合のみ処理
            # 新しいラベルを追加
            label = tk.Label(self.display_frame, text=content, anchor='w', justify='left', wraplength=480)
            label.pack(anchor='w', pady=2)
            self.display_texts.append(label)

            # テキストボックスをクリア
            self.post_text.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = User(root)
    app.mainloop()
