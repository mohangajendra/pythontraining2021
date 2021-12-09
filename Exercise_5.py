#Exercise 5 List Overlap
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,56,23,11,11,11,11,11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,11,23,11]
print(a)
print(b)
c=[]
if len(a)>len(b):
	for i in b:
		if i in a and i not in c:
			c.append(i)
else:
	for i in b:
		if i in b and i not in c:
			c.append(i)
print(c)
	

