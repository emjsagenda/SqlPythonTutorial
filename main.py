import mysql.connector
import json
  
f = open('config.json')
data = json.load(f)
  
mydb = mysql.connector.connect(
    host=data['host'],
    user=data['user'],
    password=data['password']
)

if mydb.is_connected():
    print("The Connection Was A Sucess")

f.close()