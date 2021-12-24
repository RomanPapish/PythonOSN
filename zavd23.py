#Напишіть програму на Python для обчислення найбільшого спільного дільника (НСД) двох натуральних чисел.  
def nsd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
        print('a = %s' % a)
        print('b = %s' % b)
        print('t = %s' % t)
    print(t)

nsd(15, 10)