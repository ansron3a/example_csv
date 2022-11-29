import csv

csv_file = []


# Открыть файл
def file_open(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))


# Добавление
def insert(bilet, fio, gender, age, tel, email, group, course):
    try:
        csv_file.append({'номер билета': bilet,
                         'фио': fio,
                         'пол': gender,
                         'возраст': age,
                         'телефон': tel,
                         'почта': email,
                         'группа': group,
                         'курс': course})
    except Exception as e:
        return f"Ошибка при добавлении записи {e}"
    print("Данные добавлены")


# Вывод всех записей
def show_rows():
    if len(csv_file) > 0:
        print('{:<14}{:<17}{:<4}{:<8}{:<12}{:<17}{:<10}{:<10}'.format('номер билета', 'фио', 'пол', 'возраст', 'телефон',
                                                                    'почта', 'группа','курс'))
        for el in csv_file:
            print('{:<14}{:<17}{:<4}{:<8}{:<12}{:<17}{:<10}{:<10}'.format(el['номер билета'], el['фио'], el['пол'],
                                                                        el['возраст'], el['телефон'], el['почта'],
                                                                        el['группа'],el['курс']))
