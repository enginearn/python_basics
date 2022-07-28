#!/usr/bin/env python3

import csv
import json
import os
import shutil
import sys

ENCODING = 'utf-8_sig'
DELIMITER = ','
extension = ''

pre = 'sample_'

def get_file_name_from_user_input():
    file_name = input('Enter file name: ')
    dir_name, file_name = os.path.split(file_name)
    if dir_name == '':
        dir_name = os.getcwd()
    extension = os.path.splitext(file_name)[1]
    print(f"File Path: {dir_name}")
    print(f"File Name: {file_name}")
    print(f"File Ext: {extension}")

    return dir_name, file_name, extension

def read_csv(file_name):
    with open(file_name, 'r', encoding=ENCODING) as f:
        reader = csv.reader(f, delimiter=DELIMITER)
        header = [next(reader) for i in range(1)]
        print(f"Header: {header}")
        list_1 = reader[0]
        list_2 = reader[1]
        print(f"List 1: {list_1}")
        print(f"List 2: {list_2}")

        return list_1, list_2

def read_json(file_name):
    with open(file_name, 'r', encoding=ENCODING) as f:
        data = json.load(f)
        print(f"Data: {data}")

        return data

def list_to_dict(data):
    keys = data[0]; values = data[1]
    dict_data = dict(zip(keys, values))
    print(f"Dict Data: {dict_data}")
    return dict_data

def json_from_dict_to_file(dict_data, file_name):
    with open(file_name, 'w', encoding=ENCODING) as f:
        json.dump(dict_data, f, indent=4, ensure_ascii=False)

from datetime import datetime

def parse_japanese_date(s):
    base_years = {'E': 1596, 'M': 1868, 'T': 1912, 'S': 1925, 'H': 1988, 'R': 2018}
    era = s[0]
    year, month, day = s[1:].split('.')
    year = base_years[era] + int(year)
    return datetime(year, int(month), int(day))

def main():
    dir_name, file_name, extension = get_file_name_from_user_input()
    if extension == '.csv':
        list_1, list_2 = read_csv(os.path.join(dir_name, file_name))
        dict_data = list_to_dict((list_1, list_2))
        json_from_dict_to_file(dict_data, os.path.join(dir_name, pre + file_name))
    elif extension == '.json':
        dict_data = read_json(os.path.join(dir_name, file_name))
        json_from_dict_to_file(dict_data, os.path.join(dir_name, pre + file_name))
    else:
        print('Invalid file extension')
        sys.exit(1)
    shutil.move(os.path.join(dir_name, file_name), os.path.join(dir_name, pre + file_name))

    print(parse_japanese_date('E.1868.1.1'))

if __name__ == '__main__':
    main()
    sys.exit(0)

