#!/usr/bin/env python3

import random as rnd


def split_list(content: list):
    data_len = int(len(content) * 0.7)
    data = rnd.sample(content, data_len)
    test = [
        elem
        for elem in content
        if elem not in data
    ]
    return data, test


def split_columns(content: list):
    last_column = [ln[-1] for ln in content]
    rest_column = [ln[:-1] for ln in content]
    return last_column, rest_column
