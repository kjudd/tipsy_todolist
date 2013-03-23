import sqlite3
from datetime import datetime, date, time

def connect_db():
	return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):
	c = db.cursor()
	query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""
	result = c.execute(query, (email, password, name))
	db.commit()
	return result.lastrowid

def authenticate(db, email, password):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE email = ? AND password = ?"""
	c.execute(query, (email, password))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None

def new_task(db, title, user_id):
	c = db.cursor()
	created_at = datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""
	result = c.execute(query, (title, created_at))
	db.commit()
	return result.lastrowid

def get_user(db, id):
	c = db.cursor()
	query = """SELECT * FROM Users WHERE id = ?"""
	c.execute(query, (id))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "username"]
		return dict(zip(fields, result))

	return None

def complete_task(db, id):
	c = db.cursor()
	completed_at = datetime.now()
	query = """UPDATE Tasks SET completed_at = ? where id = ?"""
	c.execute(query, (completed_at, id))
	db.commit()

def get_tasks(db, user_id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE user_id = ?"""
	c.execute(query, (user_id))
	result = c.fetchall()
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))
	else:
		query = """SELECT * FROM Tasks"""
		c.execute(query)
		result = c.fetchall()
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))

def get_task(db, id):
	c = db.cursor()
	query = """SELECT * FROM Tasks WHERE id = ?"""
	c.execute(query, (id))
	result = c.fetchone()
	fields = ["id", "title", "created_at", "completed_at", "user_id"]
	return dict(zip(fields, result))




# def main():
# 	connect_db()
# 	command = None
# 	while command != "quit":
# 		input_string = raw_input("Tipsy Database> ")
# 		tokens = input_string.split()
# 		command = tokens[0]
# 		args = tokens[1:]

# 	if command == "authenticate":
# 		authenticate(*args) 
# 	elif command == "new_user":
# 		new_user(*args)
# 	elif command == "new_task":
# 		new_task(*args)

# 	CONN.close()

# if __name__ == "__main__":
# 	main()