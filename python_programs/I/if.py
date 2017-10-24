n=int(input("enter number"))

if n%2==1:
	print("n is wired")
elif n%2==0 and n>=2 and n<=5:
    print("n is not wired")
elif n%2==0 and n>=6 and n<=20:    
    print("n is wired")
elif n%2==0 and n > 20:
    print("n is wired")
else:
    print("successfull") 

        

	