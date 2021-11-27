#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
print('Input any number: ')
a=float(input())
b=17   
dif=a-b
if dif>b:
	dif=dif*2
	print('Diferent = %s' % dif)
else:
	print('Diferent = %s' % dif)

