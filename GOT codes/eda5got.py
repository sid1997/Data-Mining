import mysql.connector
import matplotlib.pyplot as plt
from textblob import TextBlob

cnx = mysql.connector.connect(user='root', password='sid',host='localhost',	database='GameOfThrones1')
cursor = cnx.cursor()


l1 = []
cursor.execute("""SELECT id,body FROM Text where timestamp>1333312781""")
l1 = cursor.fetchall()

l2 = []
dic = {}
dicn = {}
for i in l1:
	#print(type(i[0]))
	cursor.execute("""SELECT tags FROM Tags where id = '%s'""" %(i[0]))
	#args = i[0]
	#sql = """SELECT tags FROM Tags where id = (%s)"""
	#cursor.execute(sql,args)
	l2 = cursor.fetchall()
	a = TextBlob(i[1])
	tt = a.sentiment.polarity
	if tt > 0.3:
		for j in l2:
			if j[0] in list(dic.keys()):
				dic[j[0]] = dic[j[0]] + 1
			else :
				dic[j[0]] = 1
	elif tt < -1*0.3:
		for j in l2:
			if j[0] in list(dicn.keys()):
				dicn[j[0]] = dicn[j[0]] + 1
			else :
				dicn[j[0]] = 1
	


dic_pos_tag = []
dic_pos_value = []
for w in sorted(dic, key=dic.get, reverse=True):
  dic_pos_tag.append(w)
  dic_pos_value.append(dic[w])

dic_neg_tag = []
dic_neg_value = []
for w in sorted(dicn, key=dicn.get, reverse = True):
  dic_neg_tag.append(w)
  dic_neg_value.append(dicn[w])

print('Positive tags in S7 : ')
for i in range(0,10):
	print(dic_pos_tag[i],dic_pos_value[i])

print()
print('Negative tags in S7 : ')
print()
for i in range(0,10):
	print(dic_neg_tag[i],dic_neg_value[i])

'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''


l1 = []
cursor.execute("""SELECT id,body FROM Text where timestamp<1333312781""")
l1 = cursor.fetchall()

l2 = []
dic = {}
dicn = {}
for i in l1:
	#print(type(i[0]))
	cursor.execute("""SELECT tags FROM Tags where id = '%s'""" %(i[0]))
	#args = i[0]
	#sql = """SELECT tags FROM Tags where id = (%s)"""
	#cursor.execute(sql,args)
	l2 = cursor.fetchall()
	a = TextBlob(i[1])
	tt = a.sentiment.polarity
	if tt > 0.3:
		for j in l2:
			if j[0] in list(dic.keys()):
				dic[j[0]] = dic[j[0]] + 1
			else :
				dic[j[0]] = 1
	elif tt < -1*0.3:
		for j in l2:
			if j[0] in list(dicn.keys()):
				dicn[j[0]] = dicn[j[0]] + 1
			else :
				dicn[j[0]] = 1
	


dic_pos_tag = []
dic_pos_value = []
for w in sorted(dic, key=dic.get, reverse=True):
  dic_pos_tag.append(w)
  dic_pos_value.append(dic[w])

dic_neg_tag = []
dic_neg_value = []
for w in sorted(dicn, key=dicn.get, reverse = True):
  dic_neg_tag.append(w)
  dic_neg_value.append(dicn[w])

print()
print('Positive tags in S1 : ')
print()
for i in range(0,10):
	print(dic_pos_tag[i],dic_pos_value[i])

print()
print('Negative tags in S1 : ')
print()
for i in range(0,10):
	print(dic_neg_tag[i],dic_neg_value[i])

'''
cursor.execute("""SELECT caption FROM Photo where timestamp>1333312781""")
l2 = cursor.fetchall()

cursor.execute("""SELECT body FROM Chat where timestamp>1333312781""")
l3 = cursor.fetchall()

cursor.execute("""SELECT text FROM Quote where timestamp>1333312781""")
l4 = cursor.fetchall()
'''
