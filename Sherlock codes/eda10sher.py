import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Arrow')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp>1450940602) t1, Tags where t1.id = Tags.id""")
l1 = cursor.fetchall()
'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''

dici = {}
dici2 = {}
for i in l1:
	if len(i[3]) >= 4:
	
		sentbody = TextBlob(i[0])
		sentbody = sentbody.sentiment.polarity
		senttag = TextBlob(i[3])
		senttag = senttag.sentiment.polarity
		xx = sentbody-senttag
		idd = i[2]
		if idd in dici :
			if xx < -1*0.1 or xx > 0.1 :
				dici[idd] = xx
		else :
			if xx < -1*0.1 or xx > 0.1 :
				dici[idd] = xx
			
		if idd in dici2 :
			if xx > -1*0.1 and xx < 0.1 :
				dici2[idd] = xx
		else :
			if xx > -1*0.1 and xx < 0.1 :
				dici2[idd] = xx
			




dicu5 = {}
for i in l1:
	time = i[1]
	ide = i[2]
	if ide in dicu5.keys():
		dicu5[ide] = time
	else :
		dicu5[ide] = time





loo_pos2 = []
loo_neg2 = []
liss = []
liss = [1482665189 ,1483356895, 1483961695, 1484566495]
for i in range(1,len(liss)+1):
	le = []
	le2 = []
	for j in dicu5.keys():
		if int(dicu5[j]) < liss[i-1]+604800 and int(dicu5[j]) >= liss[i-1] :
			if j in dici.keys() :
				le.append(dici[j])
			if j in dici2.keys():
				le2.append(dici2[j])
			
	loo_pos2.append(len(le))
	loo_neg2.append(len(le2))


print(loo_pos2)
print(loo_neg2)


names = ['Trailer','Episode 1','Episode 2','Episode 3']


x = np.array([0,1,2,3])
plt.xticks(x, names)
plt.title('SEASON 4')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s7sher.png')
plt.show()




lu1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp<1450940602) t1, Tags where t1.id = Tags.id""")
lu1 = cursor.fetchall()
'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''
dic = {}
dic2 = {}
for i in lu1:
	if len(i[3]) >= 4:
	
		sentbody = TextBlob(i[0])
		sentbody = sentbody.sentiment.polarity
		senttag = TextBlob(i[3])
		senttag = senttag.sentiment.polarity
		xx = sentbody-senttag
		idd = i[2]
		if idd in dic :
			if xx < -1*0.1 or xx > 0.1 :
				dic[idd] = xx
		else :
			if xx < -1*0.1 or xx > 0.1 :
				dic[idd] = xx
			
		if idd in dic2 :
			if xx > -1*0.1 and xx < 0.1 :
				dic2[idd] = xx
		else :
			if xx > -1*0.1 and xx < 0.1 :
				dic2[idd] = xx
			




dicu2 = {}
for i in lu1:
	time = i[1]
	ide = i[2]
	if ide in dicu2.keys():
		dicu2[ide] = time
	else :
		dicu2[ide] = time




loo_pos2 = []
loo_neg2 = []
liss2 = []

liss2 = [1387971295 ,1388662495, 1389267295, 1389872095]

#print(dicu2)
#print(dicu4)

for i in range(1,len(liss2)+1):
	le = []
	le2 = []
	for j in dicu2.keys():
		if int(dicu2[j]) < liss2[i-1]+604800 and int(dicu2[j]) >= liss2[i-1] :
			
			if j in dic.keys() :
				le.append(dic[j])
			if j in dic2.keys():
				le2.append(dic2[j])
		
	loo_pos2.append(len(le))
	loo_neg2.append(len(le2))
print(loo_pos2)
print(loo_neg2)


names = ['Trailer','Episode 1','Episode 2','Episode 3']


x = np.array([0,1,2,3])
plt.xticks(x, names)
plt.title('SEASON 3')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s1sher.png')
plt.show()

