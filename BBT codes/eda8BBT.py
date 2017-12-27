from collections import Counter
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Sherlock')
cursor = cnx.cursor()

l = []
l1 = []
l2 = []

cursor.execute("""SELECT blog_name FROM Text where timestamp>1411385659""")
l1 = cursor.fetchall()
cursor.execute("""SELECT blog_name FROM Photo where timestamp>1411385659""")
l2 = cursor.fetchall()


dic1 = {}

print('SEASON 10 STARTS: ')

print()
print()

for i in l1:
	if i in dic1.keys():
		val = dic1[i]
		dic1[i] = val + 1
	else :
		dic1[i] = 1

dic2 = {}

for i in l2:
	if i in dic2.keys():
		val = dic2[i]
		dic2[i] = val + 1
	else :
		dic2[i] = 1

dic3 = {}
for i in dic1.keys():
	if i in dic2.keys():
		dic3[i] = dic1[i]/dic2[i]

lis = []
for w in sorted(dic3, key=dic3.get, reverse=True):
  lis.append(w)

for i in range(0,10):
	print(lis[i],dic3[lis[i]])

print()
print()

lio = []
for w in sorted(dic3, key=dic3.get, reverse=False):
  lio.append(w)

for i in range(0,10):
	print(lio[i],dic3[lio[i]])


print()
print()
print()
print('SEASON 6 STARTS : ')
print()
print()
print()


lu = []
lu1 = []
lu2 = []


cursor.execute("""SELECT blog_name FROM Text where timestamp<1411385659""")
lu1 = cursor.fetchall()
cursor.execute("""SELECT blog_name FROM Photo where timestamp<1411385659""")
lu2 = cursor.fetchall()


dicu1 = {}

for i in lu1:
	if i in dicu1.keys():
		val = dicu1[i]
		dicu1[i] = val + 1
	else :
		dicu1[i] = 1

dicu2 = {}

for i in lu2:
	if i in dicu2.keys():
		val = dicu2[i]
		dicu2[i] = val + 1
	else :
		dicu2[i] = 1

dicu3 = {}
for i in dicu1.keys():
	if i in dicu2.keys():
		dicu3[i] = dicu1[i]/dicu2[i]

lisu = []
for w in sorted(dicu3, key=dicu3.get, reverse=True):
  lisu.append(w)

for i in range(0,10):
	print(lisu[i],dicu3[lisu[i]])

print()
print()

lio = []
for w in sorted(dicu3, key=dicu3.get, reverse=False):
  lio.append(w)

for i in range(0,10):
	print(lio[i],dicu3[lio[i]])
