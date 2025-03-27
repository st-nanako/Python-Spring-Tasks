    def post_message(self):
        # テキストボックスから内容を取得
        content = self.post_text.get("1.0", "end").strip()
        if content:  # 空白以外なら処理
            self.post_text_list.insert(0,content)
            # 投稿フレームをリセット
            for widget in self.posts_frame.winfo_children():  # posts_frame内の全てのウィジェットを取得
                widget.destroy()  # 各ウィジェットを削除

            for text in self.post_text_list:
                print(text)
                # 投稿フレームを作成
                post_frame = tk.Frame(self.posts_frame, bg="#f0f0f0", pady=5)
                post_frame.pack(fill="x", pady=5)

                # アイコン画像の読み込みと表示
                user_img = Image.open("user.png").resize((50, 50))  # サイズを調整
                user_icon = ImageTk.PhotoImage(user_img)

                icon_label = tk.Label(post_frame, image=user_icon)
                icon_label.image = user_icon  # 参照を保持
                icon_label.pack(side="left", padx=5)

                heart_img = Image.open("ハート(なし).png").resize((30, 30))  # サイズを調整
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