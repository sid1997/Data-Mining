import mysql.connector
import numpy as np
import matplotlib.pyplot as plt


cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Sherlock')
cursor = cnx.cursor()

lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp<1411385659""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp<1411385659""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp<1411385659""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp<1411385659""")
l4 = cursor.fetchall()


for i in l1:
	lu.append(i)

for i in l2:
	lu.append(i)

for i in l3:
	lu.append(i)

for i in l4:
	lu.append(i)

loo_pos = []

'''
lis = []
lis = [1498015802,1500287402,1500892202,1501497002,1502101802,1502706602,1503311402,1503916202,1703916202]
for i in range(1,len(lis)):
	op = []
	for j in lu:
		if int(j[0])<lis[i] and int(j[0])>lis[i-1]:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7']


x = np.array([0,1,2,3,4,5,6,7])
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.show()
'''
lis = []
lis = [1347017695, 1348832095, 1349436895, 1350041695, 1350646495, 1351251295, 1351856095, 1352460895, 1353065695,  1354275295, 1354880095, 1355484895,  1357299295, 1357904095, 1359718495, 1360323295, 1360928095, 1361532895,  1362742495, 1363347295, 1365161695, 1366976095, 1367580895, 1368185695, 1368790495]
for i in range(1,len(lis)+1):
	op = []
	for j in lu:
		if int(j[0])>=lis[i-1] and int(j[0])<lis[i-1]+604800:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.title('SEASON 6')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s6_BBT.png')
plt.show()









lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp>1411385659""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp>1411385659""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp>1411385659""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp>1411385659""")
l4 = cursor.fetchall()


for i in l1:
	lu.append(i)

for i in l2:
	lu.append(i)

for i in l3:
	lu.append(i)

for i in l4:
	lu.append(i)

loo_pos = []

'''
lis = []
lis = [1498015802,1500287402,1500892202,1501497002,1502101802,1502706602,1503311402,1503916202,1703916202]
for i in range(1,len(lis)):
	op = []
	for j in lu:
		if int(j[0])<lis[i] and int(j[0])>lis[i-1]:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7']


x = np.array([0,1,2,3,4,5,6,7])
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.show()
'''
lis = []
lis = [1472556895, 1474371295, 1474976095, 1475580895, 1476185695, 1476790495, 1477654495, 1478259295, 1478864095, 1479468895, 1480678495, 1481888095, 1483702495, 1484912095, 1486121695, 1486726495, 1487331295, 1487936095, 1489145695, 1490960095, 1491564895, 1492169695, 1493379295, 1493984095, 1494588895]
for i in range(1,len(lis)+1):
	op = []
	for j in lu:
		if int(j[0])<lis[i-1]+604800 and int(j[0])>=lis[i-1]:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.title('SEASON 10')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s10_BBT.png')
plt.show()