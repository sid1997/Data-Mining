import mysql.connector
import numpy as np
import matplotlib.pyplot as plt


cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Homeland')
cursor = cnx.cursor()

lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp>1355812421""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp>1355812421""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp>1355812421""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp>1355812421""")
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
lis = [1481974495, 1484566495, 1485171295, 1485776095, 1486985695, 1487590495, 1488195295, 1488800095, 1489404895, 1490009695, 1490614495, 1491219295, 1491824095]
for i in range(1,len(lis)+1):
	op = []
	for j in lu:
		if int(j[0])>=lis[i-1] and int(j[0])<lis[i-1]+604800:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.title('SEASON 6')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s6home.png')
plt.show()









lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp<1355812421""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp<1355812421""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp<1355812421""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp<1355812421""")
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
lis = [1302348895, 1317641695, 1318246495, 1318851295,1319456095, 1320060895, 1320665695,1321270495,1321875295,1322480095,1323084895,1323689695,1324294495,1324899295]
for i in range(1,len(lis)):
	op = []
	for j in lu:
		if int(j[0])<lis[i] and int(j[0])>lis[i-1]:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.title('SEASON 1')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s1home.png')
plt.show()