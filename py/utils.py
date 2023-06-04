#!/usr/bin/env python3

from dashtable import data2rst as tab


def formating_float(ls: list):
    return [
        format(n, '.3f') + '%'
        for n in ls
    ]


def formating_content(content: list[list]):
    return [
        [x[0].capitalize()] + formating_float(x[1:])
        for x in content
    ]


def generate_table(content: list[list]):
    hdr = [
        ['BD', 'KNN', '', '', 'Arbol de decision'],
        ['', 'k=1', 'k=3', 'k=5', '']
    ]
    spans = [
        [[0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0]],
        [[0, 4], [1, 4]]
    ]
    hdr.extend(
        sorted(
            formating_content(content),
            key=lambda x: x[0]
        )
    )
    table = tab(
        hdr, spans,
        use_headers=True,
        center_headers=True
    )
    print(table)


def calculate_similarity_percentage(ls1: list, ls2: list):
    similarity = sum(
        x == y
        for x, y in zip(ls1, ls2)
    )
    return (similarity / len(ls1)) * 100
