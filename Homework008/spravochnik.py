import json

glav_menu = {1:'Открыть файл',
             2:'Сохранить файл',
             3:'Посмотреть все контакты',
             4:'Создать контакт',
             5:'Найти контакт',
             6:'Изменить контакт',
             7:'Удалить контакт',
             8:'Выход'}
print('Главное меню: ')

for key, value in glav_menu.items():
    print("{0}: {1}".format(key,value))

n = int(input('Введите пункт меню: '))

if n < 1 or n > 8:
    print('Такого пункта в меню нет')
else:
    for key in glav_menu:
        if key == 1 == n:
            def open_cont():
                my_sprav = open('spravoch.txt', 'r', encoding='UTF-8')
                my_sprav.close()
            open_cont()
        elif key == 2 == n:
            def save_cont():
                phone_book = []
                my_sprav = open('spravoch.txt', 'r', encoding='UTF-8')
                data = my_sprav.readlines()
                my_sprav.close()

                for contact in data:
                    new_contact = contact.strip().split(';')
                    new_contact = {'name':new_contact[0],
                    'phone':new_contact[1],
                    'comment':new_contact[2]}
                    phone_book.append(new_contact) 
                with open('spravoch.json','w',encoding='UTF-8') as fp: 
                    json.dump(phone_book,fp,ensure_ascii=False, indent=4) 
        elif key == 3 == n:
            def read_cont():
                with open('spravoch.txt', 'r', encoding='UTF-8') as my_sprav:
                    for line in my_sprav:
                        print(line.strip())
            read_cont()
        elif key == 4 == n:
            def add_contack():
                file = open('spravoch.txt', 'a',encoding = 'UTF-8')
                data1 = input('Введите ФИО: ')
                data2 = input('Номер телефона: ')
                data3 = input('Комментарий: ')
                data = '\n' + data1 + ';' + data2 + ';' + data3
                print(data)
                file.write(data)
                file.close()
            add_contack()
        elif key == 5 == n:
            def find_cont():
                my_sprav = open('spravoch.txt', 'r', encoding='UTF-8')
                data = my_sprav.readlines()
                my_sprav.close()
                search_count = input('Введите информацию для поиска: ')
                for cont in data:
                    if search_count.lower() in cont.lower():
                            print(cont)
            find_cont()
        elif key == 6 == n:
            def izm_cont():
                my_sprav = open('spravoch.txt', 'rt', encoding='UTF-8')
                data = my_sprav.read()
                old_name = input('Что хотите изменить: ')
                new_name = input('На что хотите заменить: ')
                data = data.replace(old_name,new_name)
                my_sprav.close()
                my_sprav = open('spravoch.txt', 'wt', encoding='UTF-8')
                my_sprav.write(data)
                my_sprav.close()
            izm_cont()
        elif key == 7 == n:
            def delete_cont():
                with open('spravoch.txt', 'r', encoding='UTF-8') as file:
                    lines = file.readlines()
                s = int(input('Введите номер строки для удаления: '))
                s = s-1
                if s > len(lines):
                    print('Ошибка')
                else:
                    del lines[s]
                    with open('spravoch.txt', 'w', encoding='UTF-8') as file:
                        file.writelines(lines)
            delete_cont()
        elif key == 8 == n:
            def close_cont():
                my_sprav = open('spravoch.txt', 'r', encoding='UTF-8')
                my_sprav.close()
                close_cont() 
