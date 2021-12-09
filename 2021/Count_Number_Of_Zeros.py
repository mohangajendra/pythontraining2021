# # #count number of zeros in a list without using any list functions or a temp list.
# a=[1,2,0,0,3,4,50,6,0,0,19,398]
# length=len(a)
# count =0
# for i in range(length):
	# if a[i]!=0:
		# a[count]=a[i]
		# count+=1		
# while count< length:
	# a[count]=0
	# count+=1
# print(a)

########

def count_zeros(a):
	length=len(a)
	count=0
	for j in range(length):
		a[j]=int(a[j])# this line to make sure the entered string from input is converted to int to count zero, else the code will not work.
	for i in range(length):
		if a[i]!=0:
			a[count]=a[i]
			count+=1		
	while count< length:
		a[count]=0
		count+=1
	print(a)
	return a

if __name__=='__main__':
	a=list(input("Enter the number sequence: "))
	b=count_zeros(a)
	print(b)