#program to reverse list
Orig=[1,2,3,4]
#Direct reversing
#print(Orig[::-1])
#with for loop
reversed_list=[]
length=len(Orig)
while(length !=0):
	reversed_list.append(Orig[length-1])
	length-=1
print(reversed_list)

#Using while when number of values are even in a list.
i=0
while(length !=0):
	reversed_list.insert(i,Orig[length-1])
	length-=1
	i+=1
print(reversed_list)


#Different and Efficient way of reversing.
A=[1,2,3,4,5]
n=len(A)
for i in range(int(n/2)):
	A[i],A[n-1]=A[n-1],A[i]
	# temp=A[i]
	# A[i]=A[n-1]
	# A[n-1]=temp
	n-=1
print(A)

#with reverse function
num=[12,13,14,15]
print(num)
print(num.reverse())
