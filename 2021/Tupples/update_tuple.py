#update tuple by adding 4 to each item

test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

for item in range(len(test_list)):
	temp_list=list(test_list[item])
	num=4
	for element in range(len(temp_list)):
		temp_list[element]+=num
	test_list[item]=(tuple(temp_list))
print(test_list)
	
	















# for i in test_list:
	# dummy=list(i)
	# print(dummy)
	# for j in range(len(dummy)):
		# dummy[j]+=4
		# print(dummy)
	# dummy=tuple(i)
	# print(dummy)
# print(test_list)