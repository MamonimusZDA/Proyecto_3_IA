#!/usr/bin/env python3

import random as rnd


def split_list(content: list):
    data_len = int(len(content) * 0.7)
    train = rnd.sample(content, data_len)
    test = [
        elem
        for elem in content
        if elem not in train
    ]
    return train, test


def split_columns(content: list):
    last_column = [ln[-1] for ln in content]
    rest_column = [ln[:-1] for ln in content]
    return rest_column, last_column


def merge_lists(ls1: list, ls2: list):
    return [
        [a, b]
        for a, b in zip(ls1, ls2)
    ]
