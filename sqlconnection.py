import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="coderprem",
  database="crud"
)

#insert the data
def insert(name,age,city):
  res=mydb.cursor()
  sql="insert into user(Name,Age,City)values(%s,%s,%s)"
  user=(name,age,city)
  res.execute(sql,user)
  mydb.commit()
  print("Data insert successfully!")
#updating the data
def update(name,age,city,id):
  res = mydb.cursor()
  sql = "update user set Name=%s,Age=%s,City=%s where id=%s"
  user = (name, age, city, id)
  res.execute(sql, user)
  mydb.commit()
  print("Data update successfully!")
#select the data
def select():
  res=mydb.cursor()
  sql="select ID,Name,Age,City from user"
  res.execute(sql)
  result=res.fetchall()
  print(tabulate(result,headers=["ID","Name","Age","City"]))
#delete the data
def delete(id):
  res = mydb.cursor()
  sql = "delete from user where id=%s"
  user = (id,)
  res.execute(sql, user)
  mydb.commit()
  print("Data deleted successfully!")

while True:
  print("1.Insert the data")
  print("2.Update the data")
  print("3.Select the data")
  print("4.Delete the data")
  print("5.Quit")
  choice=int(input("Enter Your Choice:"))

  if choice==1:
    name=input("Enter Your Name:")
    age=int(input("Enter Your Age:"))
    city=input("Enter Your City name:")
    insert(name,age,city)
  elif choice==2:
    id= int(input("Enter Your Id:"))
    name=input("Enter Your Name:")
    age=int(input("Enter Your Age:"))
    city=input("Enter Your City name:")
    update(name,age,city,id)
  elif choice==3:
    select()
  elif choice==4:
    id=int(input("Enter the ID to delete:"))
    delete(id)
  elif choice==5:
    quit()
  else:
    print("INVALID SELECTION")
    print("!!!!!!!!!!!!!!!!!!")
