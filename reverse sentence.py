# your code goes here
# your code goes here
# your code goes here
alphabet = input("Enter the string")
data = alphabet.split() #split string into a list
n=len(data)
for i in range(n):
	if i%2==0:
		print(data[i])
	else:
		temp=data[i]
		print(temp[::-1])
