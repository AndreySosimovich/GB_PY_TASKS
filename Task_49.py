

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')
    while (choice != 6):
        if choice == 1:
            print_text(phone_book)
        elif choice == 2:
            find_data(phone_book)
        elif choice == 3:
            import_file = input('Введите имя файла: ')
            import_data(import_file, 'phonebook.txt')
        elif choice == 4:
            export_file = input('Введите имя файла: ')
            export_data(export_file, 'phonebook.txt')
        elif choice == 5:
            write_txt('phonebook.txt')
        choice = show_menu()


def show_menu():
    print('1. Распечатать справочник\n'
          '2. Поиск \n'
          '3. Импортировать данные\n'
          '4. Экспортировать данные\n'
          '5. Добавить абонента в справочник\n'
          '6. Закончить работу')
    choice = int(input())
    return choice


def find_menu():
    print('Выбериет параметр поиска: ')
    search_par = input(
        '1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n4 - по комментарию\n')
    print()
    search_data = 0
    if search_par == '1':
        search_data = input('Введите фамилию: ')
        print()
    elif search_par == '2':
        search_data = input('Введите имя: ')
        print()
    elif search_par == '3':
        search_data = input('Введите номер: ')
        print()
    elif search_par == '4':
        search_data = input('Введите комментарий: ')
    return search_par, search_data


def find_data(phonebook):
    search_par, search_data = find_menu()
    search_dict = {'1': 'Фамилия', '2': 'Имя',
                   '3': 'Телефон', '4': 'Комментарий'}
    find_result = []
    for name in phonebook:
        if name[search_dict[search_par]] == search_data:
            find_result.append(name)
    if len(find_result) == 0:
        print('Контакт не найден!')
    else:
        print_text(find_result)
    print()


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Комментарий']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split()))
            phone_book.append(record)
    return phone_book


def print_text(text_print):
    x = text_print
    a, *b = x
    print(*a, sep=' '*4)
    for text in text_print:
        for key, value in text.items():
            print(f'{value:10}', end='')
        print()


def import_data(text_add, phonebook):
    try:
        with open(text_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            num_str = input('Введите номер строки: ')
            contacts_to_add = new_contacts.readlines(num_str)
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{text_add} не найден')


def export_data(text_exp, phonebook):
    with open(text_exp, 'w', encoding='utf-8') as new_contacts, open(phonebook, 'r', encoding='utf-8') as file:
        num_str = [int(input('Введите номер строкb: '))]
        print(num_str)
        for lines, line in enumerate(file):
            if lines + 1 in num_str:
                new_contacts.write(line)


def add_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    description_user = input('Добавте комментарий: ')
    print(last_name, first_name, phone_number, description_user)
    return last_name, first_name, phone_number, description_user


def write_txt(filename):
    text = ' '.join(add_user())
    with open(filename, 'a', encoding='utf-8') as phout:
        phout.write(f'{text}\n')


work_with_phonebook()
