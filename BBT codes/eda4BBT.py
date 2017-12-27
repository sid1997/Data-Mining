import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Sherlock')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp<1411385659""")
l1 = cursor.fetchall()

'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''
dic = {}
for i in l1:
	dic[i[1]] = i[0] 

#dicpol = {}

lis_pos = []
lis_neg = []
for i in l1:
	t = TextBlob(dic[i[1]])
	a = t.sentiment.polarity
	if a > 0.3:
		lis_pos.append(i[1])

	if a < -1*0.3:
		lis_neg.append(i[1])


loo_tot = []
loo_pos = []
loo_neg = []
lis = []
lis = [1347017695, 1348832095, 1349436895, 1350041695, 1350646495, 1351251295, 1351856095, 1352460895, 1353065695,  1354275295, 1354880095, 1355484895,  1357299295, 1357904095, 1359718495, 1360323295, 1360928095, 1361532895,  1362742495, 1363347295, 1365161695, 1366976095, 1367580895, 1368185695, 1368790495]
for i in range(1,len(lis)+1):
	op = []
	for j in lis_pos:
		if int(j)>=lis[i-1] and int(j)<lis[i-1]+604800:
			op.append(j)
		
	loo_pos.append(len(op))
	
	oq = []
	for j in lis_neg:
		if int(j)>=lis[i-1] and int(j)<lis[i-1]+604800:
			oq.append(j)
		
	loo_neg.append(len(oq))
	loo_tot.append(len(op)+len(oq))


print(loo_pos)
print(loo_neg)

names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.xticks(x, names)
plt.title('SEASON 6')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc = 'upper left')
plt.savefig('4s6_BBT.png')
plt.show()




l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp>1411385659""")
l1 = cursor.fetchall()
'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''
dic = {}
for i in l1:
	dic[i[1]] = i[0] 

#dicpol = {}

lis_pos = []
lis_neg = []
for i in l1:
	t = TextBlob(dic[i[1]])
	a = t.sentiment.polarity
	if a > 0.3 :
		lis_pos.append(i[1])

	if a < -1*0.3:
		lis_neg.append(i[1])


loo_tot = []
loo_pos = []
loo_neg = []
lis = []
lis = [1472556895, 1474371295, 1474976095, 1475580895, 1476185695, 1476790495, 1477654495, 1478259295, 1478864095, 1479468895, 1480678495, 1481888095, 1483702495, 1484912095, 1486121695, 1486726495, 1487331295, 1487936095, 1489145695, 1490960095, 1491564895, 1492169695, 1493379295, 1493984095, 1494588895]
for i in range(1,len(lis)+1):
	op = []
	for j in lis_pos:
		if int(j)<lis[i-1]+604800 and int(j)>=lis[i-1]:
			op.append(j)
		
	loo_pos.append(len(op))
	
	oq = []
	for j in lis_neg:
		if int(j)<lis[i-1]+604800 and int(j)>=lis[i-1]:
			oq.append(j)
		
	loo_neg.append(len(oq))
	loo_tot.append(len(op)+len(oq))


print(loo_pos)
print(loo_neg)

names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.xticks(x, names)
plt.title('SEASON 10')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc='upper left')
plt.savefig('4s10_BBT.png')
plt.show()

