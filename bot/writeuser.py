import sqlite3
import datetime

def create_db(chat_id: int, first_name: str, second_name: str, tele_login: str):
	telebase = sqlite3.connect('crate/DB/teleusers.sqlite3', check_same_thread=False)
	telebase_cursor = telebase.cursor()
	telebase_cursor.execute('INSERT INTO users (chat_id, first_name, second_name, tele_login, Date_start) VALUES (?, ?, ?, ?, ?)', (chat_id, first_name, second_name, tele_login, datetime.now()))
	telebase.commit()
	return print("200-OK")
