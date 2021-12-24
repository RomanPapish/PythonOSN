def fail_list(): 
    first_list=['A','B,','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    repet = 1
    while repet == 1:
    
        print('Виберіть який метод будете виконувати:\n 1.Додавання до списку.\n 2.Сортування списку.\n 3.Видалення елменту з списку.\n 4.Оберне6ння елментів списку.\n 5.Визначення кількості елементів.')
        item = int(input())
    
        if item == 1:
    
            el_1 = input('Введіть елемент який хочете додати: ')
            first_list.append(el_1)
            print(first_list)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 2:
        
            first_list.sort()
            print(first_list)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 3:
    
            print(first_list)
            el_1 = input('Введіть елемент який хочете видалити: ')
            first_list.remove(el_1)
            print(first_list)
        
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 4:
    
            print(first_list)
            first_list.reverse()
            print(first_list)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 5:
    
            el_1 = input('Введіть елемент кількічть якого хочете підрахувати: ')
            s = first_list.count(el_1)
            print('Кількість елементів в списку: %s' % s)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())