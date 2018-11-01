'''кция принимает аргументБпроверить тип.Если это не список или кортежБ выводить значение типа
если же кортеж или списокБ то нужно определить длину.
Если она больше 1Б то вывести информацию о томБ сколько разных типов данных там содержиться'''

counttypes = 0
types = []
A = list([1,24.0,3,2,[],(),3,'str',4])

def IdentificationList(A):
	if type(A) != tuple or type(A) != list:
		print('тип аргумента = ' + str(type(A)))
	else:
		print('длинна листа(кортежа) равна = ' + len(A))
		
IdentificationList(A)

if type(A) == tuple or type(A) == list:	
	def CountType(A):
		if len(A) > 1:
			for i in A:
				if type(i) not in types:
					types.append(type(i))
		return types

	CountType(A)
	counttypes = len(types)
	print(counttypes)




