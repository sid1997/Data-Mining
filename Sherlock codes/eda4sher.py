import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Arrow')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp FROM Text where timestamp<1450940602""")
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
lis = [1387971295 ,1388662495, 1389267295, 1389872095]
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

names = ['Trailer','Episode 1','Episode 2','Episode 3']

x = np.array([0,1,2,3])
plt.xticks(x, names)
plt.title('SEASON 3')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc = 'upper left')
plt.savefig('4s3_sher.png')
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
lis = [1482665189 ,1483356895, 1483961695, 1484566495]
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

names = ['Trailer','Episode 1','Episode 2','Episode 3']


x = np.array([0,1,2,3])
plt.xticks(x, names)
plt.title('SEASON 4')
plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos,'-o',color='b',label = 'Positive reviews')
plt.plot(x,loo_neg,'-o',color='r',label = 'Negative reviews')
plt.legend(loc='upper left')
plt.savefig('4s4_sher.png')
plt.show()

