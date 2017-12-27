import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import plotly.plotly as py
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='GameOfThrones1')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp,note_count FROM Text where timestamp>1333312781""")
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
lis_pos_nc = []
lis_neg = []
lis_neg_nc = []
for i in l1:
	t = TextBlob(dic[i[1]])
	a = t.sentiment.polarity
	if a > 0.3 :
		lis_pos.append(i[1])
		lis_pos_nc.append(i[2])
	if a < -1*0.3:
		lis_neg.append(i[1])
		lis_neg_nc.append(i[2])


#loo_pos = []
loo_pos_nc = []
loo_neg_nc = []
#loo_neg = []
lis = []
lis = [1499682602,1500287402,1500892202,1501497002,1502101802,1502706602,1503311402,1503916202,1504521002]
for i in range(1,len(lis)):
	#op = []
	ncp = 0
	for j in range(0,len(lis_pos)):
		if int(lis_pos[j])<lis[i] and int(lis_pos[j])>lis[i-1]:
			#op.append(lis_pos[int(j)])
			ncp = ncp + int(lis_pos_nc[j])
	#loo_pos.append(len(op))
	loo_pos_nc.append(ncp)
	
	#oq = []
	ncn = 0
	for j in range(0,len(lis_neg)):
		if int(lis_neg[j])<lis[i] and int(lis_neg[j])>lis[i-1]:
			#oq.append(lis_neg[j])
			ncn = ncn + int(lis_neg_nc[j])
	#loo_neg.append(len(oq))
	loo_neg_nc.append(ncn)

#loo_pos_nc.sort(reverse=True)
#loo_neg_nc.sort(reverse=True)
loo_tot_nc = []
for i in range(0,8):
	print(loo_pos_nc[i])
	print(loo_neg_nc[i])
	loo_tot_nc.append(loo_pos_nc[i]+loo_neg_nc[i])

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7']


x = np.array([0,1,2,3,4,5,6,7])
plt.xticks(x, names)
plt.plot(x, loo_tot_nc,'-o',color='g',label='Total reviews')
plt.plot(x, loo_pos_nc,'-o',color='b',label='Positive reviews')
plt.plot(x,loo_neg_nc,'-o',color='r',label='Negative reviews')
plt.legend(loc='upper left')
plt.savefig('7s7got.png')
plt.show()



l1 = []
cursor.execute("""SELECT body,timestamp,note_count FROM Text where timestamp<1333312781""")
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
lis_pos_nc = []
lis_neg = []
lis_neg_nc = []
for i in l1:
	t = TextBlob(dic[i[1]])
	a = t.sentiment.polarity
	if a > 0.3 :
		lis_pos.append(i[1])
		lis_pos_nc.append(i[2])
	if a < -1*0.3:
		lis_neg.append(i[1])
		lis_neg_nc.append(i[2])


#loo_pos = []
loo_pos_nc = []
loo_neg_nc = []
#loo_neg = []
lis = []
lis = [1302517130,1303121930,1303726730,1304331530,1304936330,1305541130,1306145930,1306750730,1307355530,1307960330,1308565130,1309169930]
for i in range(1,len(lis)):
	#op = []
	ncp = 0
	for j in range(0,len(lis_pos)):
		if int(lis_pos[j])<lis[i] and int(lis_pos[j])>lis[i-1]:
			#op.append(lis_pos[int(j)])
			ncp = ncp + int(lis_pos_nc[j])
	#loo_pos.append(len(op))
	loo_pos_nc.append(ncp)
	
	#oq = []
	ncn = 0
	for j in range(0,len(lis_neg)):
		if int(lis_neg[j])<lis[i] and int(lis_neg[j])>lis[i-1]:
			#oq.append(lis_neg[j])
			ncn = ncn + int(lis_neg_nc[j])
	#loo_neg.append(len(oq))
	loo_neg_nc.append(ncn)

#loo_pos_nc.sort(reverse=True)
#loo_neg_nc.sort(reverse=True)
loo_tot_nc = []
for i in range(0,11):
	print(loo_pos_nc[i])
	print(loo_neg_nc[i])
	loo_tot_nc.append(loo_pos_nc[i]+loo_neg_nc[i])

names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7','Episode 8','Episode 9','Episode 10']


x = np.array([0,1,2,3,4,5,6,7,8,9,10])
plt.xticks(x, names)
plt.plot(x, loo_tot_nc,'-o',color='g',label='Total reviews')
plt.plot(x, loo_pos_nc,'-o',color='b',label='Positive reviews')
plt.plot(x,loo_neg_nc,'-o',color='r',label='Negative reviews')
plt.legend(loc='upper left')
plt.savefig('7s1_got.png')
plt.show()


