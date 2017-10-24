if __name__ == '__main__':
    N = int(input())
    # number of command lines
    for i in range(0,N):
        if i%1==0 and (i%i==0 or i%2!=0):
           print("i is prime number")
        elif i%1==0 and (i%i==0 or i%2==0):
           print("i is prime number")