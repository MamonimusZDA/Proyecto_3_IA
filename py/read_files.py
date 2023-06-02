#! /usr/bin/env python3

import os
import re
import platform


def get_delimiter():
    match platform.system():
        case 'Linux':
            return '/'
        case 'Darwin':
            return '/'
        case 'Windows':
            return '\\'


def get_data_path():
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    prev_dir = os.path.dirname(curr_dir)
    delim = get_delimiter()
    return '{}{}data{}'.format(
        prev_dir, delim, delim
    )


def convert_number_values(line: list):
    tmp_line = []
    for x in line:
        try:
            x = float(x)
            tmp_line.append(x)
        except ValueError:
            tmp_line.append(x)
    return tmp_line


def read_data(file_name: str):
    data_path = get_data_path()
    data_file = data_path + file_name
    with open(data_file, 'r') as file:
        lines = file.read().split('\n')
        lines = [ln.split(',') for ln in lines]
        return [
            convert_number_values(ln)
            for ln in lines if len(ln) > 1
        ]


def list_data_files():
    data_path = get_data_path()
    return os.listdir(data_path)


def get_name_files(files: list):
    pattern = r'\.\w+$'
    return [
        re.sub(pattern, '', f)
        for f in files
    ]


def get_data_files_content():
    contents = {}
    files = list_data_files()
    files_name = get_name_files(files)
    for f, fn in zip(files, files_name):
        contents[fn] = read_data(f)
    return contents
