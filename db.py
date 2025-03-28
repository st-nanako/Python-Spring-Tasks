import random
import hashlib
import MySQLdb
# ソルトの生成
def get_salt():
    random_source = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt = ''
    for _ in range(16):
        salt += random.choice(random_source)

    return salt
# パスワードのハッシュ
def get_hadhed_password(plain_pw,salt):
    hashed_pw = hashlib.pbkdf2_hmac('sha256',plain_pw.encode(),salt.encode(),19720).hex()
    for _ in range(198):
        hashed_pw = hashlib.pbkdf2_hmac('sha256',plain_pw.encode(),salt.encode(),19720).hex()
    
    return hashed_pw

def get_connection():
    connection = MySQLdb.connect(user="root",
                                password = "iluka3",
                                host = "localhost",
                                database = "python_sns")
    return connection
# ユーザーの登録
def insert_user(name,email,pw,icon):
    salt = get_salt() # saltを生成
    hashed_pw = get_hadhed_password(pw,salt) #　PWをハッシュ
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO users(id,name,mail,pw,salt) VALUES(DEFAULT,%s,%s,%s,%s)"
    cursor.execute(sql,(name,email,hashed_pw,salt))
    
    sql2 = "INSERT INTO user_icon(id,user_id, user_icon_path) VALUES(DEFAULT,LAST_INSERT_ID(), %s)"
    cursor.execute(sql2, (icon,))
    
    connection.commit()
    cursor.close()
    connection.close()
# パスワード再設定
def re_pass(email,pw):
    salt = get_salt() # saltを生成
    hashed_pw = get_hadhed_password(pw,salt) #　PWをハッシュ
    connection = get_connection()
    cursor = connection.cursor()
    sql = "UPDATE users SET pw = %s,salt = %s WHERE mail = %s"
    
    cursor.execute(sql,(hashed_pw,salt,email))
    
    connection.commit()
    cursor.close()
    connection.close()

# ユーザーの編集
def edit_user(id,name,email):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "UPDATE users SET name = %s,mail = %s WHERE id = %s"
    
    cursor.execute(sql,(name,email,id))
    
    connection.commit()
    cursor.close()
    connection.close()
# ユーザーの編集（PW）
def edit_user_pw(id,name,email,pw):
    salt = get_salt() # saltを生成
    hashed_pw = get_hadhed_password(pw,salt) #　PWをハッシュ
    connection = get_connection()
    cursor = connection.cursor()
    sql = "UPDATE users SET name = %s,mail = %s,pw = %s,salt = %s WHERE id = %s"
    
    cursor.execute(sql,(name,email,hashed_pw,salt,id))
    
    connection.commit()
    cursor.close()
    connection.close()
    
# アカウントのメールの取得
def get_account_by_email(email):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT id,name,mail,pw,salt FROM users WHERE mail = %s"
    
    cursor.execute(sql,(email,))
    account = cursor.fetchone()
    cursor.close()
    connection.close()
    
    return account
# ログイン処理
def login(email,input_pw):
    account = get_account_by_email(email) #DBからアカウント情報を取得
    # アカウント情報が取得できない場合はログイン失敗
    if account is None:
        return None #ログイン失敗
    
    hashed_db_pw = account[3] #DBから取得したハッシュ済みのpw
    salt = account[4] #DBから取得したsalt
    hashed_input_pw = get_hadhed_password(input_pw,salt) #入力されたpwをハッシュ
    
    if hashed_db_pw == hashed_input_pw:
        return account #ログイン成功
    else:
        return None #ログイン失敗
    
# 本の登録
def insert_book(title,author,status):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO books(id,title,author,Loan_status) VALUES(DEFAULT,%s,%s,%s)"
    
    cursor.execute(sql,(title,author,status))
    
    connection.commit()
    cursor.close()
    connection.close()
# 本の削除
def del_book(id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "DELETE FROM books WHERE id = %s"
    cursor.execute(sql,(id,))
    
    connection.commit()
    cursor.close()
    connection.close()
# 全ての本
def select_books():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT * FROM books"
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    
    return rows
# 本の検索
def search_books(word):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT * FROM books WHERE title LIKE %s or author LIKE %s"
    cursor.execute(sql,("%"+word+"%","%"+word+"%"))
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    
    return rows
# 本の編集
def edit_book(id,title,author):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "UPDATE books SET title = %s,author = %s WHERE id = %s"
    cursor.execute(sql,(title,author,id))
    
    connection.commit()
    cursor.close()
    connection.close()
# 本の貸出
def lending_book(user_id,book_id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO lending_return(id,user_id,book_id,lending_date) VALUES(DEFAULT,%s,%s,now())"
    
    cursor.execute(sql,(user_id,book_id))
    
    connection.commit()
    cursor.close()
    connection.close()

# 本の貸出状況ステータス変更
def book_status(book_id,status):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "UPDATE books SET Loan_status = %s WHERE id = %s"
    
    cursor.execute(sql,(status,book_id))
    
    connection.commit()
    cursor.close()
    connection.close()

# 貸出中の本
def select_currently_renting_book():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT books.id,title,author FROM books INNER JOIN  lending_return ON books.id = lending_return.book_id WHERE lending_return.return_date IS NULL"
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    
    return rows
# ユーザーが借りている本
def select_user_rending(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT books.id,title,author FROM books LEFT OUTER JOIN lending_return ON books.id = lending_return.book_id WHERE lending_return.return_date IS NULL AND lending_return.user_id = %s"
    cursor.execute(sql,(user_id,))
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    
    return rows

# 本の返却
def return_book(user_id,book_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "UPDATE lending_return SET return_date = now() WHERE user_id = %s AND book_id = %s"
    cursor.execute(sql,(user_id,book_id))
    
    connection.commit()
    cursor.close()
    connection.close()

# 貸出可 
def loanable():
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT id, title, author FROM books WHERE books.id NOT IN (SELECT book_id FROM lending_return WHERE return_date IS NULL)"
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    return rows

# ユーザーの貸出履歴
def lending_log(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT books.id,title,author FROM books LEFT OUTER JOIN lending_return ON books.id = lending_return.book_id WHERE lending_return.return_date IS NOT NULL AND lending_return.user_id = %s"
    cursor.execute(sql,(user_id,))
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    return rows

# 貸出可の本の検索
def loanable_book_search(word):
    connection = get_connection()
    cursor = connection.cursor()
    
    sql = "SELECT id, title, author FROM books WHERE id NOT IN (SELECT book_id FROM lending_return WHERE return_date IS NULL) AND (title LIKE %s or author LIKE %s)"
    cursor.execute(sql,("%" + word + "%","%" + word + "%"))
    
    rows = cursor.fetchall()
    
    # コネクションを切断
    cursor.close()
    connection.close()
    return rows