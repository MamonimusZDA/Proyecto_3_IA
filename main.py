#! /usr/bin/env python3

from py.read_files import get_data_files_content
from py import utils

import py.db_manipulation as dbm


def main():
    content = get_data_files_content()
    for c in content:
        print(content[c])


if __name__ == '__main__':
    main()
