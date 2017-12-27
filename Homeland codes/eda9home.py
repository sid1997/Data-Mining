from collections import Counter
import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import numpy as np
import pandas as pd

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='Homeland')
cursor = cnx.cursor()

l = []
l1 = []
l2 = []
l3  = []
l4  = []
l5 = []

cursor.execute("""SELECT note_count FROM Text where timestamp>1355812421""")
l1 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Photo where timestamp>1355812421""")
l2 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Quote where timestamp>1355812421""")
l3 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Chat where timestamp>1355812421""")
l4 = cursor.fetchall()
#cursor.execute("""SELECT note_count FROM Answer where timestamp>1333312781""")
#l5 = cursor.fetchall()


median = []
median2 = []

l34 = []
for i in l1:
	l34.append(i[0])

l34.sort()
median.append('Text')
median2.append(l34[len(l34)//2])

l34 = []
for i in l2:
	l34.append(i[0])

l34.sort()
median.append('Photo')
median2.append(l34[len(l34)//2])

l34 = []
for i in l3:
	l34.append(i[0])

l34.sort()
median.append('Quote')
median2.append(l34[len(l34)//2])

l34 = []
for i in l4:
	l34.append(i[0])

l34.sort()
median.append('Chat')
median2.append(l34[len(l34)//2])


print(median)
print(median2)




summ = {}

sl1 = 0
#print(l1)
for i in l1:
	sl1 = sl1+int(i[0])
summ['Text'] = sl1

sl2 = 0
for i in l2:
	sl2 = sl2+int(i[0])
summ['Photo'] = sl2

sl3 = 0
for i in l3:
	sl3 = sl3+int(i[0])
summ['Quote'] = sl3

sl4 = 0
for i in l4:
	sl4 = sl4+int(i[0])
summ['Chat'] = sl4

#sl5 = 0
#for i in l5:
#	sl5 = sl5+int(i[0])
#summ['Answer'] = sl5



maxx = {}

sl1 = 0
for i in l1:
	if int(i[0])>sl1:
		sl1 = int(i[0])
maxx['Text'] = sl1

sl2 = 0
for i in l2:
	if int(i[0])>sl2:
		sl2 = int(i[0])
maxx['Photo'] = sl2

sl3 = 0
for i in l3:
	if int(i[0])>sl3:
		sl3 = int(i[0])
maxx['Quote'] = sl3

sl4 = 0
for i in l4:
	if i[0]>sl4:
		sl4 = int(i[0])
maxx['Chat'] = sl4

#sl5 = 0
#for i in l5:
	#if int(i[0])>sl5:
	#	sl5 = int(i[0])
#maxx['Answer'] = sl5


minn = {}

sl1 = 1000000000
for i in l1:
	if int(i[0])<sl1:
		sl1 = int(i[0])
minn['Text'] = sl1

sl2 = 1000000000
for i in l2:
	if int(i[0])<sl2:
		sl2 = int(i[0])
minn['Photo'] = sl2

sl3 = 1000000000
for i in l3:
	if int(i[0])<sl3:
		sl3 = int(i[0])
minn['Quote'] = sl3

sl4 = 1000000000
for i in l4:
	if int(i[0])<sl4:
		sl4 = int(i[0])
minn['Chat'] = sl4

"""sl5 = 1000000000
for i in l5:
	if int(i[0])<sl5:
		sl5 = int(i[0])
minn['Answer'] = sl5
"""
print(maxx)
print(minn)
print(summ)

maxx1 = []
maxx2 = []
for i in maxx.keys():
	maxx1.append(i)
	maxx2.append(maxx[i])

print(maxx1)
print(maxx2)

summ1 = []
summ2 = []
for i in summ.keys():
	summ1.append(i)
	summ2.append(summ[i])

print(summ1)
print(summ2)


#naam = {'first_name' : ['text','image','chat','quote']}
#df = pd.DataFrame(raw_data, columns = ['first_name', 'Sum of Note_Counts', 'Max of Note_Counts'])
#pos = list(range(len(summ)))
#width = 0.25
x = np.array([0,1,2,3])
plt.bar(x,summ2,color='g',label='Sum of Note_Counts')
plt.title('SEASON 6')
#plt.bar(x,maxx2,color='b',label='Max of Note_Counts')
#plt.y_label('Note_Counts')
plt.xticks(x, summ1)
plt.legend(loc='upper left')
plt.savefig('9s6sum_home.png')
plt.show()

plt2.bar(x,maxx2,color='g',label='Max of Note_Counts')
plt2.xticks(x,maxx1)
plt2.title('SEASON 6')
plt2.legend(loc='upper left')
plt2.savefig('9s6max_home.png')
plt2.show()

plt3.bar(x,median2,color='g',label='Median of Note_Counts')
plt3.xticks(x,median)
plt3.title('SEASON 6')
plt3.legend(loc='upper left')
plt3.savefig('9s6median_home.png')
plt3.show()


print()
print()
print()
print('SEASON 1 STARTS : ')
print()
print()
print()


l = []
l1 = []
l2 = []
l3  = []
l4  = []
l5 = []

cursor.execute("""SELECT note_count FROM Text where timestamp<1355812421""")
l1 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Photo where timestamp<1355812421""")
l2 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Quote where timestamp<1355812421""")
l3 = cursor.fetchall()
cursor.execute("""SELECT note_count FROM Chat where timestamp<1355812421""")
l4 = cursor.fetchall()
#cursor.execute("""SELECT note_count FROM Answer where timestamp<1333312781""")
#l5 = cursor.fetchall()


summu = {}

sl1 = 0
for i in l1:
	sl1 = sl1+int(i[0])
summu['Text'] = sl1

sl2 = 0
for i in l2:
	sl2 = sl2+int(i[0])
summu['Photo'] = sl2

sl3 = 0
for i in l3:
	sl3 = sl3+int(i[0])
summu['Quote'] = sl3

sl4 = 0
for i in l4:
	sl4 = sl4+int(i[0])
summu['Chat'] = sl4
"""
sl5 = 0
for i in l5:
	sl5 = sl5+int(i[0])
summu['Answer'] = sl5
"""


maxxu = {}

sl1 = 0
for i in l1:
	if int(i[0])>sl1:
		sl1 = int(i[0])
maxxu['Text'] = sl1

sl2 = 0
for i in l2:
	if int(i[0])>sl2:
		sl2 = int(i[0])
maxxu['Photo'] = sl2

sl3 = 0
for i in l3:
	if int(i[0])>sl3:
		sl3 = int(i[0])
maxxu['Quote'] = sl3

sl4 = 0
for i in l4:
	if int(i[0])>sl4:
		sl4 = int(i[0])
maxxu['Chat'] = sl4
"""
sl5 = 0
for i in l5:
	if int(i[0])>sl5:
		sl5 = int(i[0])
maxxu['Answer'] = sl5
"""

minnu = {}

sl1 = 1000000000
for i in l1:
	if int(i[0])<sl1:
		sl1 = int(i[0])
minnu['Text'] = sl1

sl2 = 1000000000
for i in l2:
	if int(i[0])<sl2:
		sl2 = int(i[0])
minnu['Photo'] = sl2

sl3 = 1000000000
for i in l3:
	if int(i[0])<sl3:
		sl3 = int(i[0])
minnu['Quote'] = sl3

sl4 = 1000000000
for i in l4:
	if int(i[0])<sl4:
		sl4 = int(i[0])
minnu['Chat'] = sl4
"""
sl5 = 1000000000
for i in l5:
	if int(i[0])<sl5:
		sl5 = int(i[0])
minnu['Answer'] = sl5
"""

maxx1 = []
maxx2 = []
for i in maxxu.keys():
	maxx1.append(i)
	maxx2.append(maxxu[i])

print(maxx1)
print(maxx2)

summ1 = []
summ2 = []
for i in summu.keys():
	summ1.append(i)
	summ2.append(summu[i])

print(summ1)
print(summ2)

median = []
median2 = []

l34 = []
for i in l1:
	l34.append(i[0])

l34.sort()
median.append('Text')
median2.append(l34[len(l34)//2])

l34 = []
for i in l2:
	l34.append(i[0])

l34.sort()
median.append('Photo')
median2.append(l34[len(l34)//2])

l34 = []
for i in l3:
	l34.append(i[0])

l34.sort()
median.append('Quote')
median2.append(l34[len(l34)//2])

l34 = []
for i in l4:
	l34.append(i[0])

l34.sort()
median.append('Chat')
median2.append(l34[len(l34)//2])


print(median)
print(median2)


#naam = {'first_name' : ['text','image','chat','quote']}
#df = pd.DataFrame(raw_data, columns = ['first_name', 'Sum of Note_Counts', 'Max of Note_Counts'])
#pos = list(range(len(summ)))
#width = 0.25
x = np.array([0,1,2,3])
plt.bar(x,summ2,color='g',label='Sum of Note_Counts')
plt.title('SEASON 1')
#plt.bar(x,maxx2,color='b',label='Max of Note_Counts')
#plt.y_label('Note_Counts')
plt.xticks(x, maxx1)
plt.legend(loc='upper left')
plt.savefig('9s1sum_home.png')
plt.show()

plt2.bar(x,maxx2,color='g',label='Max of Note_Counts')
plt2.title('SEASON 1')
plt2.xticks(x,maxx1)
plt2.legend(loc='upper left')
plt2.savefig('9s1max_home.png')
plt2.show()

plt3.bar(x,median2,color='g',label='Median of Note_Counts')
plt3.xticks(x,median)
plt3.title('SEASON 1')
plt3.legend(loc='upper left')
plt3.savefig('9s1median_home.png')
plt3.show()
