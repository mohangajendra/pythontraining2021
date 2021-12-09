##print any item that is repeatig in a list nd count the number of times it repeated
"""a=[1,2,3,4,5,2,4,6,7,2,1,4,5]
b={}
for i in a:
	if i in b:
		b[i]+=1
	else:
		b[i]=1
print(b)

value_max=0
key_max=''

##now from here get the highest key and values

for key, value in b.items():
	if value > value_max:
		value_max=value
		key_max=key
print("{} is occuring max number of times with {} count".format(key_max, value_max))"""

###redoing this as function

def number_of_ocurrence(a):
	b={}
	for i in a:
		if i in b:
			b[i]+=1
		else:
			b[i]=1
	value_max=0
	key_max=''

	##now from here get the highest key and values

	for key, value in b.items():
		if value > value_max:
			value_max=value
			key_max=key
	return value_max, key_max
	print("{} is occuring max number of times with {} count".format(key_max, value_max))
	
if __name__=='__main__':
	a=list(input("Enter the list"))
	print(type(a))
	value_max, key_max=number_of_ocurrence(a)
	print("{} is occuring max number of times with {} count".format(key_max, value_max))