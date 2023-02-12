import sqlite3

con = sqlite3.connect('data_base/db_bot.db')
cur = con.cursor()


def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS phone_book 
                (id_pb INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR, phone_number VARCHAR, comment VARCHAR, 
                price NUMERIC(4,2))''')
    con.commit()

def insert_new_user(user: tuple):
    cur.execute('''INSERT INTO phone_book (name, phone_number, 
                comment, price) VALUES (?, ?, ?, ?)''', user)
    con.commit()

def select_user(criterion: str):
    result = cur.execute('''SELECT name, phone_number 
                        FROM phone_book 
                        WHERE comment=?''',(criterion,)).fetchall()
    return result

def update_user(original: str, new: str):
    cur.execute('''UPDATE phone_book SET name=? 
                        WHERE name=?''',(new, original))
    con.commit()

def delete_user(criterion: str, value: str):
    cur.execute(f'''DELETE FROM phone_book WHERE {criterion}=?''', (value,))
    con.commit()