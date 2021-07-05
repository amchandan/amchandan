def  lisupper(items="default"):
	names = []
	for item in items:
		if item[0]==item[0].upper():
			names.append(item)

	return names

	

			
print(lisupper(["Ram","sita","HARI","Gudu"])