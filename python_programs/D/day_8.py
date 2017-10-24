s={'Rithika':'6692646227','Raju':'6509227343','Girija':'8019329367','Rithurajeswar':'7989710472'}

t= {'Rithika', 'Ramu', 'Rithurajeswar'}

for x in t:
	print(s.get(x))
	print((s.get(x) == 'None'))
	if(s.get(x) == 'None'):
		print 'Not Found'
	else: 
		print(str(x)+ '='+str(s.get(x)))

	# print(s.get(x, 'Not Found'))

# for key,value in s.items():
# 	print key, value

# print(s.get('Rithika','not found'))
# print(s.get('Raju','not found'))
# print(s.get('Girija','not found'))
# print(s.get('Rithurajeswar','not found'))
# print(s.get('Revathi','not found'))