import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='GameOfThrones1')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp>1333312781) t1, Tags where t1.id = Tags.id""")
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
	if len(i[3]) > 4:
	
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
liss = [1499682602,1500287402,1500892202,1501497002,1502101802,1502706602,1503311402,1503916202,1504521002]
for i in range(1,len(liss)):
	le = []
	le2 = []
	for j in dicu5.keys():
		if int(dicu5[j]) < liss[i] and int(dicu5[j]) > liss[i-1] :
			if j in dici.keys() :
				le.append(dici[j])
			if j in dici2.keys():
				le2.append(dici2[j])
			
	loo_pos2.append(len(le))
	loo_neg2.append(len(le2))


print(loo_pos2)
print(loo_neg2)


names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7']


x = np.array([0,1,2,3,4,5,6,7])
plt.xticks(x, names)
plt.title('SEASON 7')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s7got.png')
plt.show()




lu1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp<1333312781) t1, Tags where t1.id = Tags.id""")
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
	if len(i[3]) > 4:
	
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

liss2 = [1302517130,1303121930,1303726730,1304331530,1304936330,1305541130,1306145930,1306750730,1307355530,1307960330,1308565130,1309169930]

#print(dicu2)
#print(dicu4)

for i in range(1,len(liss2)):
	le = []
	le2 = []
	for j in dicu2.keys():
		if int(dicu2[j]) < liss2[i] and int(dicu2[j]) > liss2[i-1] :
			
			if j in dic.keys() :
				le.append(dic[j])
			if j in dic2.keys():
				le2.append(dic2[j])
		
	loo_pos2.append(len(le))
	loo_neg2.append(len(le2))
print(loo_pos2)
print(loo_neg2)


names = ['Trailer','Episode 1','Episode 2','Episode 3','Episode 4','Episode 5','Episode 6','Episode 7','Episode 8','Episode 9','Episode 10']


x = np.array([0,1,2,3,4,5,6,7,8,9,10])
plt.xticks(x, names)
plt.title('SEASON 1')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s1got.png')
plt.show()

