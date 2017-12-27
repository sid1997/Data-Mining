import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='GameOfThrones1')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp>1333312781""")
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
lis = [1499682602,1500287402,1500892202,1501497002,1502101802,1502706602,1503311402,1503916202,1504521002]
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

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7']


x = np.array([0,1,2,3,4,5,6,7])
plt.xticks(x, names)
plt.title('SEASON 7')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc='upper left')
plt.savefig('4s7got.png')
plt.show()




l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp<1333312781""")
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
lis = [1302517130,1303121930,1303726730,1304331530,1304936330,1305541130,1306145930,1306750730,1307355530,1307960330,1308565130,1309169930]
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

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7','Episode 8','Episode 9','Episode 10']


x = np.array([0,1,2,3,4,5,6,7,8,9,10])
plt.xticks(x, names)
plt.title('SEASON 1')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc='upper left')
plt.savefig('4s1got.png')
plt.show()

