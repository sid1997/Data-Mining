import mysql.connector
import numpy as np
import matplotlib.pyplot as plt


cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Arrow')
cursor = cnx.cursor()

lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp<1450940602""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp<1450940602""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp<1450940602""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp<1450940602""")
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
lis = [1387971295 ,1388662495, 1389267295, 1389872095]
for i in range(1,len(lis)+1):
	op = []
	for j in lu:
		if int(j[0])>=lis[i-1] and int(j[0])<lis[i-1]+604800:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','Episode 1','Episode 2','Episode 3']


x = np.array([0,1,2,3])
plt.title('SEASON 3')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s3_sher.png')
plt.show()









lu = []
l1 = []
l2 = []
l3 = []
l4 = []
cursor.execute("""SELECT timestamp FROM Text where timestamp>1450940602""")
l1 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Photo where timestamp>1450940602""")
l2 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Chat where timestamp>1450940602""")
l3 = cursor.fetchall()

cursor.execute("""SELECT timestamp FROM Quote where timestamp>1450940602""")
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
lis = [1482665189 ,1483356895, 1483961695, 1484566495]
for i in range(1,len(lis)+1):
	op = []
	for j in lu:
		if int(j[0])<lis[i-1]+604800 and int(j[0])>=lis[i-1]:
			op.append('h')
		
	loo_pos.append(len(op))

print(loo_pos)

names = ['Trailer','Episode 1','Episode 2','Episode 3']


x = np.array([0,1,2,3])
plt.title('SEASON 4')
plt.xticks(x, names)
plt.plot(x, loo_pos,'-o',color='g')
plt.savefig('1s4_sher.png')
plt.show()