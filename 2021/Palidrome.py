## verify if the given input is palindrome
def palidrome(seq):
	temp_seq=list(seq)
	length=len(temp_seq)
	rev_seq=''
	for i in range(length):
		rev_seq=rev_seq+temp_seq[length-i-1]
	#print(rev_seq)
	rev_seq=str(rev_seq)
	if rev_seq==seq:
		print(" {} is a palidrome,".format(seq))
	else:
		print(" {} is NOT a palidrome,".format(seq))

if __name__=='__main__':
	seq=input("Enter the string to verify if the given data is palindrome: ")
	palidrome(seq)
	