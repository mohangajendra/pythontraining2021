#Palindrome
n_str=input("pls enter value you want to check:")
q=''
for i in range(len(n_str)):
	q=q+n_str[len(n_str)-1-i]
print(q)
if n_str==q:
	print(n_str+ " is palindrome")
else:
	print(n_str+ " is NOT a palindrome")

##Palindrome simplified.
new_str=reversed(n_str)
if n_str==new_str:
	print(n_str+ " is palindrome")
else:
	print(n_str+ " is NOT a palindrome")

##Palindrome 

m_str=n_str[::-1]
if n_str==m_str:
	print(n_str+ " is palindrome")
else:
	print(n_str+ " is NOT a palindrome")
