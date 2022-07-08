import sqlite3

db_connection =sqlite3.connect('todoList.db')
with open('schema.sql') as sql_file:
    table_script=sql_file.read()
db_connection.executescript(table_script)
cur=db_connection.cursor()

todo_list=[['project_creation','create a python project whose deadliine in november'],
['hackerrank contest','participate in hackerrank contest daily'],
['flask coding','create one portfolio based app. using flask']]

for todo in todo_list:
    cur.execute('INSERT INTO todo(title, todoDesc) VALUES (?, ?)', (todo[0], todo[1]))

db_connection.commit()
cur.close()
db_connection.close()