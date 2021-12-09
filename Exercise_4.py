#Divisor
num=int(input("Provide the number you want find divisor of:"))
divisor=[]
listRange = list(range(2,int(num/2)+1))
for div in listRange:
	if num%div==0:
		divisor.append(div)
print("Here are the list of divisors for " + str(num) + ": \n")
print(divisor)
