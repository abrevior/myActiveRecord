import mysql

list = mysql.select_user()
for row in list:
    print(row[1])