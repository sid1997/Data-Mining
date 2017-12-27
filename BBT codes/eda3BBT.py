from collections import Counter
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np


cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Sherlock')
cursor = cnx.cursor()

print('SEASON 10 STARTS')

l = []
l1 = []
l2 = []
l3 = []
l4 = []


cursor.execute("""SELECT blog_name,note_count FROM Text where timestamp>1411385659""")
l1 = cursor.fetchall()
#print(l)
cursor.execute("""SELECT blog_name,note_count FROM Photo where timestamp>1411385659""")
l2 = cursor.fetchall()
cursor.execute("""SELECT blog_name,note_count FROM Chat where timestamp>1411385659""")
l3 = cursor.fetchall()
cursor.execute("""SELECT blog_name,note_count FROM Quote where timestamp>1411385659""")
l4 = cursor.fetchall()

for i in l1:
	l.append(i)

for i in l2:
	l.append(i)

for i in l3:
	l.append(i)

for i in l4:
	l.append(i)


dic = {}
for i in l:
	dic[i[0]] = i[1] 


lis = []
for w in sorted(dic, key=dic.get, reverse=True):
  lis.append(w)
  
for i in range(0,10):
	print(lis[i],dic[lis[i]])


print()
print()
print()
print('SEASON 6 STARTS ')
print()
print()
print()

#############



lu = []
lu1 = []
lu2 = []
lu3 = []
lu4 = []

cursor.execute("""SELECT blog_name,note_count FROM Text where timestamp<1411385659""")
lu1 = cursor.fetchall()
#print(l)
cursor.execute("""SELECT blog_name,note_count FROM Photo where timestamp<1411385659""")
lu2 = cursor.fetchall()
cursor.execute("""SELECT blog_name,note_count FROM Chat where timestamp<1411385659""")
lu3 = cursor.fetchall()
cursor.execute("""SELECT blog_name,note_count FROM Quote where timestamp<1411385659""")
lu4 = cursor.fetchall()


for i in lu1:
	lu.append(i)

for i in lu2:
	lu.append(i)

for i in lu3:
	lu.append(i)

for i in lu4:
	lu.append(i)

dic2 = {}
for i in lu:
	dic2[i[0]] = i[1] 


lis2 = []
for w in sorted(dic2, key=dic2.get, reverse=True):
  lis2.append(w)
  
for i in range(0,10):
	print(lis2[i],dic2[lis2[i]])



