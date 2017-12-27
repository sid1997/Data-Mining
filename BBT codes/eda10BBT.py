import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Sherlock')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp>1411385659) t1, Tags where t1.id = Tags.id""")
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
			if sentbody>0 and senttag<0 :
				dici[idd] = xx
		else :
			if sentbody<0 and senttag>0 :
				dici[idd] = xx
			
		if idd in dici2 :
			if sentbody>0 and senttag>0 :
				dici2[idd] = xx
		else :
			if sentbody<0 and senttag<0 :
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
liss = [1472556895, 1474371295, 1474976095, 1475580895, 1476185695, 1476790495, 1477654495, 1478259295, 1478864095, 1479468895, 1480678495, 1481888095, 1483702495, 1484912095, 1486121695, 1486726495, 1487331295, 1487936095, 1489145695, 1490960095, 1491564895, 1492169695, 1493379295, 1493984095, 1494588895]
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


names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.xticks(x, names)
plt.title('SEASON 10')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s10BBT.png')
plt.show()




lu1 = []
cursor.execute("""SELECT body,t1.timestamp, t1.id, tags from(SELECT body,timestamp,id FROM Text where timestamp<1411385659) t1, Tags where t1.id = Tags.id""")
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
			if sentbody>0 and senttag<0 :
				dic[idd] = xx
		else :
			if sentbody<0 and senttag>0 :
				dic[idd] = xx
			
		if idd in dic2 :
			if sentbody>0 and senttag>0 :
				dic2[idd] = xx
		else :
			if sentbody<0 and senttag<0 :
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

lis = [1347017695, 1348832095, 1349436895, 1350041695, 1350646495, 1351251295, 1351856095, 1352460895, 1353065695,  1354275295, 1354880095, 1355484895,  1357299295, 1357904095, 1359718495, 1360323295, 1360928095, 1361532895,  1362742495, 1363347295, 1365161695, 1366976095, 1367580895, 1368185695, 1368790495]

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


names = ['Trailer','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','E24']


x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
plt.xticks(x, names)
plt.title('SEASON 6')
#plt.plot(x, loo_tot,'-o',color='g',label = 'Total reviews')
plt.plot(x, loo_pos2,'-o',color='b',label = 'Tags Body Agree')
plt.plot(x,loo_neg2,'-o',color='r',label = 'Tags Body Disagree')
plt.legend(loc='upper left')
plt.savefig('10s6BBT.png')
plt.show()

