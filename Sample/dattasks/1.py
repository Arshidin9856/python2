import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="pp2demo",
  user="pp2demo_user",
  password="pp2demo")

cursor = conn.cursor()
# 1 и 2 задание - вывод университета и професора по айди
# sql1='SELECT version()'
# st_id=1
# pr_id=101
# sql1=f'SELECT university_name,students_count,Prof_name,speciality,salary FROM university,professor WHERE id={st_id} and uni_id={st_id};'
# sql2=f'SELECT university_name,students_count FROM university WHERE id={st_id};'

# cursor.execute(sql1)
# users = cursor.fetchall()
# cursor.execute(sql2)
# user= cursor.fetchall()
# l=['university_name','students_count','Prof_name','speciality','salary']
# for i in users:
#     print(f"professor worked at {user[0][0]} ")
#     for ind,j in enumerate(i):
#         print(f'{l[ind]} -- {j}')

# 3 задание - вывод по зарплате и профессии 
# spec='Math'
# salary= 3000
# sql1=f"SELECT Prof_name,speciality,salary FROM professor WHERE speciality = '{spec}' and salary>={salary} ;"
# cursor.execute(sql1)
# users = cursor.fetchall()
# print(users)

# 5 Task
# id=101
# age='5'
# sql1=f"UPDATE professor SET experience = {age} WHERE Prof_id  = {id};"
# sql2="select * from professor;"
# cursor.execute(sql1)
# cursor.execute(sql2)

# users = cursor.fetchall()
# for i in users:
#     for j in i:
#         if i[-1]==age:
#             print(i)
#             break
# print(users)


conn.commit() 
cursor.close()
conn.close()