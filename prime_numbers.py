#checking if given number is a prime number
n=int(input("enter a number:"))
flag=0
for i in range(2, int(n/2)):
	if n%i==0:
		flag=1
		break
if flag==1:
	print(str(n)+" is not prime")
else:
	print(str(n)+ " is a prime")
 
print(id(n)) #this is to find the memory location of a variable


