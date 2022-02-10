import csv
import os
import re
import json
import yaml

def get_data():
    os_prod_list =[]
    os_name_list =[]
    os_code_list =[]
    os_type_list =[]
    for root, dirs, files in os.walk(".txt"):
        for filename in files:
            input_data = csv.reader(open('filename', 'rb', 'cp1251'), delimiter=":")
            for row in input_data:
                column_name = row[0]
                column_name = column_name.strip()
                column_value = row[1]
                column_value = column_value.strip()
                match = re.search(r'.зготовитель\s*?.истемы', column_name)
                if match:
                    os_prod_list.append(column_value)
                match = re.search(r'.азвание\s*?ОС', column_name)
                if match:
                    os_name_list.append(column_value)
                match = re.search(r'Код\s*?.родукта', column_name)
                if match:
                    os_code_list.append(column_value)
                match = re.search(r'Тип\s*?.истемы', column_name)
                if match:
                    os_type_list.append(column_value)
    names_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [names_list]
    ultimate_len = 0
    if len(os_type_list) > len(os_code_list):
        ultimate_len = len(os_type_list)
        if ultimate_len > len(os_prod_list):
            if ultimate_len > len(os_name_list):
            else:
                ultimate_len = len(os_name_list)
        else:
            ultimate_len = len(os_prod_list)
            if ultimate_len > len(os_name_list):
            else:
                ultimate_len = len(os_name_list)
    else:
        ultimate_len = len(os_code_list)
        if ultimate_len > len(os_prod_list):
            if ultimate_len > len(os_name_list):
            else:
                ultimate_len = len(os_name_list)
        else:
            ultimate_len = len(os_prod_list)
            if ultimate_len > len(os_name_list):
            else:
                ultimate_len = len(os_name_list)
    for index in range(ultimate_len):
        rowlist = [os_prod_list[index], os_name_list[index], os_code_list[index], os_type_list[index]]
        #тут нужна еще проверка на наличие элемента в массиве по индексу и пустая строка, если ничего нет
        main_data.append(rowlist)
    return main_data

def write_to_csv_with_check():
    main_data = get_data()
    with open('main_data_write.csv', 'w') as main_file:
        main_writer = csv.writer(main_file)
        for row in main_data:
            main_writer.writerow(row)
    with open('main_data_write.csv') as f_n:
        print(f_n.read())

def write_order_to_json_with_check(item, quantity, price, buyer, date):
    new_order = {"item": item, "quantity" : quantity, "price" : price, "buyer" : buyer, "date" : date}
    with open('orders.json', 'w') as file_name_json:
        json.dump(new_order, file_name_json)
    with open('orders.json') as f_n:
        print(f_n.read())

def write_and_check_to_yaml(dict_to_yaml):
    with open('data_write.yaml', 'w') as file_name_yaml:
        yaml.dump(dict_to_yaml, file_name_yaml)

    with open('data_write.yaml') as f_n:
        print(f_n.read())

def main():
    #1
    write_to_csv_with_check()
    #2
    write_order_to_json_with_check("Cумка", "21", "142.5", "Иванова А.С.", "12.04.2021")
    #3
    dict_yaml = {
        "test_list" : [1,2,3,4,5],
        "test_number" : 15726,
        "test_dict": {"14\x8035" : 123, "612\x8035" : 1423}
    }
    write_and_check_to_yaml(dict_yaml)

if __name__ == '__main__':
    main()




