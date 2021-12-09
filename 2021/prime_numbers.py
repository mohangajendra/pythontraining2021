def check_prime(a):
    flag=0
    for i in range(2,int(a/2)):
        if a%i==0:
            flag=1
            break        
    if flag ==1:
        print("{} is not a prime number".format(a))
    else:
        print("{} is a prime number".format(a))


if __name__=='__main__':
    a=int(input("enter a number:"))
    if a<2:
	    print("Input number should be more than 1")
	    a=int(input("enter a number:"))
	    check_prime(a)
    else:
	    check_prime(a)