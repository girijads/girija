s="sample string"
x=list(s)
index=0;
evs=""
ods=""
while  index<len(x):
	if(index%2 ==0):
		if(x[index] != ' '):
			evs=evs+x[index]
	else:
		if(x[index] != ' '):
			ods=ods+x[index]
	index= index + 1
print(evs +" " +ods)

