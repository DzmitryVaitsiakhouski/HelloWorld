'''Список [16,-17,-19,2,78.2,False,False,(True),555,12,23,42,'DD']
Функция принимает на вход список
выбирает из него все int и float
составить из него новый список , отсортированный от наименьшего значения к большему'''

list = [16,-17,-19,2,78.2,False,False,(True),555,12,23,42,'DD']
newlist = []
def IntAndFloat(list):
	for i in list:
		if type(i) is int or type(i) is float:
			newlist.append(i)
	print('неотсортированный лист = ' + str(newlist))
	
def SortedList(newlist):
	n = 1 
	while n < len(newlist): 
		for i in range(len(newlist)-n): 
			if newlist[i] > newlist[i+1]: 
				newlist[i],newlist[i+1] = newlist[i+1],newlist[i] 	
		n += 1
	print('отсортированный лист = ' + str(newlist))
	
IntAndFloat(list)
SortedList(newlist)