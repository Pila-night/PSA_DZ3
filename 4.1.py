def zamena(list, dict):
    result = []  
    for item in list:
        if item in dict:
            result.append(dict[item])  
        else:
            result.append(item)
    return result  


test_list_1 = ['ctf.pnzgu.ru', 'yandex.ru', 'dpo.pnzgu.ru', 'google.com', 'moodle.pnzgu.ru', 'lk.pnzgu.ru']
test_dict_1 = {
    'ctf.pnzgu.ru': '82.179.90.12',
    'ibst.pnzgu.ru': '82.179.90.69',
    'beda.pnzgu.ru': '82.179.90.69',
    'lk.pnzgu.ru': '82.179.90.10',
    'moodle.pnzgu.ru': '82.179.90.15',
    'dpo.pnzgu.ru': '82.179.90.54'
}

test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test_dict_2 = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    11: 'одиннадцать'
}

test_list_3 = ['поганка', 'мухомор', 'подберезовик', 'груздь', 666]
test_dict_3 = {
    'поганка': False,
    'мухомор': False,
    'подберезовик': True,
    'груздь': True,
    'Рыжик': True
}


print(zamena(test_list_1, test_dict_1))
print(zamena(test_list_2, test_dict_2))
print(zamena(test_list_3, test_dict_3))
