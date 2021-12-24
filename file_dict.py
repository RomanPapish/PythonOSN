def fail_dict():
    alfavit = 'ABCDEFGHIJKLMNOPQRS'
    first_dict=dict(enumerate(alfavit))
    print(first_dict)
    repet = 1
    while repet == 1:
        print('Виберіть який метод будете виконувати:\n 1.Отримати значення за ключем.\n 2.Отримати список значень.\n 3.Витягти довільну пару з словника.\n 4.Отримати ітератор на основі ключів словника.\n 5.Очистити словник.')
        item = int(input())
        if item == 1:
        
            key_1 = int(input('Введіть ключ: '))
            val = first_dict.get(key_1)
            print('Значення ключа : %s' % val)
            
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
        
        elif item == 2:
        
            val = first_dict.values()
            print('Список значень: \n %s' % val)
        
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
        
        elif item == 3:
            val = first_dict.popitem()
            print('Випадкова пара: \n Ключ: %s Значення: %s' % val)
        
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 4:
    
            val = iter(first_dict)
            val_lst = list(val)
        
            print('Результат: \n %s' % val_lst)
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())
    
        elif item == 5:
            
            first_dict.clear()
            print('Результат: \n %s' % first_dict)
    
            print('Повторити? 1-Так, 0-Ні')
            repet = int(input())