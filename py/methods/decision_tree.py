#!/usr/bin/env python3

from operator import itemgetter


def desclassification(vals):
    num_instances = len(vals)
    num_columns = len(vals[0])
    print(num_instances)
    print(num_columns)
    l_thresholds = []
    for i in range(num_columns - 1):
        saved_result = None
        class_name = ''
        class_number = 0
        thresholds = []
        aux = None
        aux_list = sorted(vals, key=itemgetter(i))
        for j in range(num_instances):
            print(aux_list[j])
            current_result = aux_list[j][num_columns - 1]
            if saved_result is None:
                saved_result = current_result
                aux = aux_list[j][i]
                class_name = 'Class' + str(class_number)
                aux_list[j][i] = class_name
            elif saved_result != current_result:
                if aux == aux_list[j][i]:
                    aux_list[j][i] = class_name
                else:
                    thresholds.append((aux_list[j][i] + aux) / 2)
                    class_number += 1
                    aux = aux_list[j][i]
                    class_name = 'Class' + str(class_number)
                    aux_list[j][i] = class_name
        range_thresholds = (thresholds[len(thresholds) - 1] - thresholds[0])
        print(range_thresholds)
        new_thresholds = []
        class1 = thresholds[0] + (range_thresholds / 3)
        new_thresholds.append(thresholds[0])
        for k in range(1, len(thresholds) - 1):
            if thresholds[k] >= class1:
                class1 += (range_thresholds / 3)
                new_thresholds.append(thresholds[k])
        print('Thresholds', new_thresholds, 'length', len(new_thresholds))
        print('FIN')
        l_thresholds.append(new_thresholds)
    print('tontin')
    return l_thresholds
