#list all prime numbers in a for given number
def read_inputs():
	lowerlim=int(input("enter a number:"))
	higherlim=int(input("enter a number:"))
	return lowerlim , higherlim
	# if lowerlim<=1 or higherlim<=1:
	# print ("2 is the lowested Prime number, please enter a number greater than 2")
#prime number programe
# prime_num=[]
# for i in range(lowerlim, (higherlim+1)):
	# for j in range(2, i//2+1):
		# if i%j==0:
			# break
	# else:
		# prime_num.append(i)
# print(prime_num)
# print ("There are {} prime numbers between {} and {}".format (len(prime_num),lowerlim, higherlim ))


##prime listing as a fucntion call.	
def listing_prime_numers(lowerlim, higherlim):
	prime_num=[]
	for i in range(lowerlim, (higherlim+1)):
		for j in range(2, i//2+1):
			if i%j==0:
				break
		else:
			prime_num.append(i)
	print(prime_num)
	print ("There are {} prime numbers between {} and {}".format (len(prime_num),lowerlim, higherlim ))




#listing_prime_numers(lowerlim, higherlim)




if __name__ == "__main__":
	lowerlim , higherlim = read_inputs()
	if lowerlim<=1 or higherlim<=1:
		print ("2 is the lowested Prime number, please enter a number greater than 2")
		lowerlim , higherlim = read_inputs()
	listing_prime_numers(lowerlim, higherlim)
