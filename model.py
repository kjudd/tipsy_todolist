"""
model.py
"""
import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("tipsy.db")

def new_user(db, email, password, name):          
    c = db.cursor()                                     
    query = """INSERT INTO Users VALUES (NULL, ?, ?, ?)"""                                                           
    result = c.execute(query, (email, password, name))           
    db.commit()
    return result.lastrowid

def make_user(row):
	fields = ["id", "email", "password", "username"]
	return dict(zip(fields, row))

def authenticate(db, email, password):
    c = db.cursor()
    query = """SELECT * from Users WHERE email=? AND password=?"""
    c.execute(query, (email, password))
    result = c.fetchone()
    if result:
        fields = ["id", "email", "password", "name"]
        return dict(zip(fields, result))

    return None

def get_user(db, id):
	c = db.cursor()
	query = """SELECT * from Users WHERE id = ?"""
	c.execute(query, (id,))
	result = c.fetchone()
	if result:
		fields = ["id", "email", "password", "name"]
		return dict(zip(fields, result))
	else:
		print "no user found"

def new_task(db, title, user_id):
	# Given a title and a user_id, create a new task belonging to that user. Return the id of the created task
	c = db.cursor()     
	date_time= datetime.now()
	query = """INSERT INTO Tasks VALUES (NULL, ?, ?, NULL, ?)"""                                                           
	result = c.execute(query, (title, date_time, user_id))           
	db.commit()

def complete_task(db, id):
	"""Mark the task with the given task_id as being complete."""
	c = db.cursor()     
	date_time = datetime.now()
	query = """UPDATE Tasks SET completed_at = ? WHERE id = ?"""                                                           
	result = c.execute(query, (id, date_time))           
	db.commit()
	print "Task completed at %s" % date_time
	return result.lastrowid
	
def get_tasks(db, user_id):

	"""Get all the tasks matching the user_id, getting all the tasks in the system if the user_id is not provided. Returns the results as a list of dictionaries."""
	c = db.cursor()
	if user_id:
		query = """SELECT * from Tasks WHERE user_id = ?"""
		c.execute(query, (user_id,))
	else:
		query = """SELECT * from Tasks"""
		c.execute(query)
	tasks = []
	rows = c.fetchall()
	for row in rows:
		task = dict(zip(["id", "title", "created_at", "completed_at",
			"user_id"], row))
		tasks.append(task)
	return tasks
	# result = c.fetchone()
	# if result:
	# 	fields = ["id", "title", "created_at", "completed_at", "user_id"]
	# 	return dict(zip(fields, result))
	# else:
	# 	c = db.cursor()
	# 	query = """SELECT * from Tasks"""
	# 	c.execute(query, )
	# 	result = c.fetchall()
	# 	l = []
	# 	for row in result:
	# 		new_dict = {}
	# 		new_dict['id']=row[0]
	# 		new_dict['title']=row[1]
	# 		new_dict['created_at']=row[2]
	# 		new_dict['completed_at']=row[3]
	# 		new_dict['user_id']=row[4]
	# 		l.append(new_dict)
	# 	return l

def get_task(db, id):
	"""Gets a single task, given its id. Returns a dictionary of the task data."""
	c = db.cursor()
	query = """SELECT * from Tasks WHERE id = ?"""
	c.execute(query, (id,))
	result = c.fetchone()
	if result:
		fields = ["id", "title", "created_at", "completed_at", "user_id"]
		return dict(zip(fields, result))
	else:
		print "task id not found"

def make_task(row):
	columns = ["id", "title", "created_at", "completed_at", "user_id"]
	return dict(zip(columns, row))