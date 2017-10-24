if __name__ == '__main__':
    N = int(input())
    # takes input 
    list=[]
    # number of command lines
    for i in range(0,N):
        S=input()
        st=S.split(" ")
        if (st[0] == 'insert'):
        	list.insert(int(st[1]), int(st[2]))
        elif (st[0] == 'print'):
        	print(list)
        elif(st[0] == 'remove'):
        	list.remove(int(st[1]))
        elif (st[0] == 'append'):
        	list.append(int(st[1]))
        elif (st[0] == 'sort'):
            list.sort()
        elif (st[0] == 'pop'):
        	list.pop()
        elif (st[0] == 'reverse'):
        	list.reverse()