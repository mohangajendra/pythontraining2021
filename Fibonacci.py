#generating fibonacci
fibonacci=[0,1]
#print("Pls enter the number until which you need the Fibonacci Series")
n=int(input('please enter the number: '))
i=2
counter=n-2
while(counter!=0):
	fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
	i+=1
	counter-=1
print(fibonacci)
	
