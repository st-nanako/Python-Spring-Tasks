import os 
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def Register_mail(to,name):
    ID = 'n.sato.sys24@morijyobi.ac.jp'
    PASSWORD = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    body = f'こんにちは{name}さん、登録が完了しました。以下は登録情報です。\r\n\r\nユーザー名:{name}\r\n\r\n登録メールアドレス:{to}'
    # 本文のインスタンスを作成し、インスタンスに設定
    msg.attach(MIMEText(body,'html'))
    
    # 件名、送信元アドレス、送信先アドレスを設定
    msg['Subject'] = '登録完了のお知らせ'
    msg['From'] = ID
    msg['To'] = to
    
    
    # SMTP サーバインスタンスを作成、ログイン
    server = SMTP(HOST,PORT)
    server.starttls()
    server.login(ID,PASSWORD)
    
    # サーバにメールインスタンスを送信
    server.send_message(msg)
    server.quit()
    
def Rending_mail(to,name,book_taitle):
    ID = 'n.sato.sys24@morijyobi.ac.jp'
    PASSWORD = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    body = f'{name}さん、{book_taitle}の貸出が完了しました。'
    
    # 本文のインスタンスを作成し、インスタンスに設定
    msg.attach(MIMEText(body,'html'))
    
    # 件名、送信元アドレス、送信先アドレスを設定
    msg['Subject'] = '貸出完了のお知らせ'
    msg['From'] = ID
    msg['To'] = to
    
    
    # SMTP サーバインスタンスを作成、ログイン
    server = SMTP(HOST,PORT)
    server.starttls()
    server.login(ID,PASSWORD)
    
    # サーバにメールインスタンスを送信
    server.send_message(msg)
    server.quit()
# 確認コードを送信
def code_mail(to,code):
    ID = 'n.sato.sys24@morijyobi.ac.jp'
    PASSWORD = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    body = f'以下は確認コードです。{code}'
    
    # 本文のインスタンスを作成し、インスタンスに設定
    msg.attach(MIMEText(body,'html'))
    
    # 件名、送信元アドレス、送信先アドレスを設定
    msg['Subject'] = '確認コード'
    msg['From'] = ID
    msg['To'] = to
    
    
    # SMTP サーバインスタンスを作成、ログイン
    server = SMTP(HOST,PORT)
    server.starttls()
    server.login(ID,PASSWORD)
    
    # サーバにメールインスタンスを送信
    server.send_message(msg)
    server.quit()