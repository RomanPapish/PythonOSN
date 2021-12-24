import file_dict, file_list, file_str
from file_dict import fail_dict
from file_list import fail_list
from file_str import fail_str
repet = 1
while repet == 1:
    print('Виберіть яке завдання виконувати:\n 1.Методи з списками.\n 2.Методи з строками.\n 3.Методи з словниками.\n ')
    item = int(input())
    
    if item == 1:
        fail_list()
            
        print('Повторити? 1-Так, 0-Ні')
        repet = int(input())
    
    elif item == 2:
        
        fail_str()
    
        print('Повторити? 1-Так, 0-Ні')
        repet = int(input())
    
    elif item == 3:
    
        fail_dict()   
    
        print('Повторити? 1-Так, 0-Ні')
        repet = int(input())