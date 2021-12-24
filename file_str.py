def fail_str():   
    first_str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    repet = 1
    while repet == 1:
        print('Виберіть який метод будете виконувати:\n 1.Всі букви в верхній регістр.\n 2.Всі букви в нижній регістр.\n 3.Строка з букв?.\n 4.Строка з цифр?.\n 5.Обєднання двох строк.')
        item = int(input())
    
        if item == 1:
    
            al_str = first_str.upper()
            print(al_str)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 2:
        
            al_str = first_str.lower()
            print(al_str)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 3:
    
            al=first_str.isalpha()
            print('Результат: %s' % al)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 4:
    
            al=first_str.isdecimal()
            print('Результат: %s' % al)
            print(first_str)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 5:
    
            second_str = '1234567890'
            third_str = second_str + first_str
            print(third_str)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())