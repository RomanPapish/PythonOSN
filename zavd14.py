#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
print('Input three any numders: ')
a=float(input())
b=float(input())
c=float(input())
suma=a+b+c
if a==b==c:
	print('Sum of numders = %s %s %s' % (suma, suma, suma))
else:
	print('Sum of numders = %s'% suma)
