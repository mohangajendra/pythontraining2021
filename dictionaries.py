#dictionaries
from collections import namedtuple
a={'name': 'Mohan', 'age': 30}
d=[1,2,3,3,3,4,9,96,55,4,7,2,7,6,9,4,6,2,1]
print(d.counter)
for key in a:
	print (key,a[key])

for key,value in (a.items()):
	     print (key,value)
