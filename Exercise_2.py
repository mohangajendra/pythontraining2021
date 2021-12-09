#Exercise 2 Even or Odd
# num=int(input("Enter the number you wanto to check, a number above 1 or 2:"))
# if(num%2==0):
	# print("The Number " + str(num) +" given is EVEN \n")
	# if(num%4==0):
		# print("The number " + str(num) +" given is Multiple of 4 \n")
# else:
	# print("The number" + str(num) +" given is ODD \n")

def even_or_odd(num):
	if(num%2==0):
		print(" The Number {} is a even number".format(num))
	else:
		print(" The Number {} is a odd number".format(num))

if __name__=='__main__':
	num=int(input("Enter a number above 1 or 2: "))
	even_or_odd(num)