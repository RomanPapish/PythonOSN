#Напишіть програму на Python для суми двох заданих цілих чисел. Однак, якщо сума становить від 15 до 20, вона поверне 20.  
a = int(input('Введіть перше число= '))
b = int(input('Введіть друге число= '))
s=a+b
if 15 <= s <= 20:
    s = 20
    print('Сума чисел в межах від 15 до 20    \n s= %s' % s)
else:
    print('Сума чисел НЕ в межах від 15 до 20    \n s= %s' % s) 