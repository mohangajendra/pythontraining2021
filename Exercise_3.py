#Exercise 3 : List Less Than Five
numbers=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
print(numbers)
for i in numbers:
	if i<=5:
		new_list.append(i)
print(new_list)

# Ask the user for a number and return a list that contains only elements from the original list
# a that are smaller than that number given by the user.

numbers=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
print(numbers)
num=int(input("enter the number to compare and list all items smaller than that:"))
for i in numbers:
	if i<=num:
		new_list.append(i)
print(new_list)



