import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Homeland')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp>1355812421""")
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
lis = [1481974495, 1484566495, 1485171295, 1485776095, 1486985695, 1487590495, 1488195295, 1488800095, 1489404895, 1490009695, 1490614495, 1491219295, 1491824095]
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

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.xticks(x, names)
plt.title('SEASON 6')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc = 'upper left')
plt.savefig('4s6_home.png')
plt.show()




l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp<1355812421""")
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
lis = [1302348895, 1317641695, 1318246495, 1318851295,1319456095, 1320060895, 1320665695,1321270495,1321875295,1322480095,1323084895,1323689695,1324294495,1324899295]
for i in range(1,len(lis)):
	op = []
	for j in lis_pos:
		if int(j)<lis[i] and int(j)>lis[i-1]:
			op.append(j)
		
	loo_pos.append(len(op))
	
	oq = []
	for j in lis_neg:
		if int(j)<lis[i] and int(j)>lis[i-1]:
			oq.append(j)
		
	loo_neg.append(len(oq))
	loo_tot.append(len(op)+len(oq))


print(loo_pos)
print(loo_neg)

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.xticks(x, names)
plt.title('SEASON 1')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc='upper left')
plt.savefig('4s1_home.png')
plt.show()

