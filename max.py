def max():	
	list = [5,'sort',2,7,4,'key',0,9,'kit',8,6]
	li = []
	for i in list:
		if type(i) == int:
			li.append(i)
	print(li)
	n = 1 
	while n < len(li): 
		for i in range(len(li)-n): 
			if li[i] > li[i+1]: 
				li[i],li[i+1] = li[i+1],li[i] 	
		n += 1
	del(li[0:7])
	print(li)
	
max()





		
