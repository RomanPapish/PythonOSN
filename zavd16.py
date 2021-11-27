#Write a Python program to count the number 4 in a given list.
#print('Input any numders: ')
stroka=input('Input any numders(n,n,n,n,n...,n): ')
stroka=stroka.split(',')
print(stroka)
countnumb=stroka.count('4')
print('Count of number 4: %s' % countnumb)
