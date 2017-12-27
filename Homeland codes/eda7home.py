import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob
import plotly.plotly as py
import matplotlib.pyplot as plt

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Homeland')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,timestamp,note_count FROM Text where timestamp>1355812421""")
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
lis = [1481974495, 1484566495, 1485171295, 1485776095, 1486985695, 1487590495, 1488195295, 1488800095, 1489404895, 1490009695, 1490614495, 1491219295, 1491824095]
for i in range(1,len(lis)+1):
	#op = []
	ncp = 0
	for j in range(0,len(lis_pos)):
		if int(lis_pos[j])>=lis[i-1] and int(lis_pos[j])<lis[i-1]+604800:
			#op.append(lis_pos[int(j)])
			ncp = ncp + int(lis_pos_nc[j])
	#loo_pos.append(len(op))
	loo_pos_nc.append(ncp)
	
	#oq = []
	ncn = 0
	for j in range(0,len(lis_neg)):
		if int(lis_neg[j])>=lis[i-1] and int(lis_neg[j])<lis[i-1]+604800:
			#oq.append(lis_neg[j])
			ncn = ncn + int(lis_neg_nc[j])
	#loo_neg.append(len(oq))
	loo_neg_nc.append(ncn)

#loo_pos_nc.sort(reverse=True)
#loo_neg_nc.sort(reverse=True)
loo_tot_nc = []
for i in range(0,13):
	print(loo_pos_nc[i])
	print(loo_neg_nc[i])
	loo_tot_nc.append(loo_pos_nc[i]+loo_neg_nc[i])

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.xticks(x, names)
plt.title('SEASON 6')
plt.plot(x, loo_tot_nc,'-o',color='g',label = 'Note_Counts of Total reviews')
plt.plot(x, loo_pos_nc,'-o',color='b',label = 'Note_Counts of Positive reviews')
plt.plot(x,loo_neg_nc,'-o',color='r',label = 'Note_Counts of Negative reviews')
plt.legend(loc='upper left')
plt.savefig('7s6_home.png')
plt.show()



l1 = []
cursor.execute("""SELECT body,timestamp,note_count FROM Text where timestamp<1355812421""")
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
lis = [1302348895, 1317641695, 1318246495, 1318851295,1319456095, 1320060895, 1320665695,1321270495,1321875295,1322480095,1323084895,1323689695,1324294495,1324899295]
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
for i in range(0,13):
	print(loo_pos_nc[i])
	print(loo_neg_nc[i])
	loo_tot_nc.append(loo_pos_nc[i]+loo_neg_nc[i])

names = ['Trailer','E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.xticks(x, names)
plt.title('SEASON 1')
plt.plot(x, loo_tot_nc,'-o',color='g',label = 'Note_Counts of Total reviews')
plt.plot(x, loo_pos_nc,'-o',color='b',label = 'Note_Counts of Positive reviews')
plt.plot(x,loo_neg_nc,'-o',color='r',label = 'Note_Counts of Negative reviews')
plt.legend(loc='upper left')
plt.savefig('7s1_home.png')
plt.show()


