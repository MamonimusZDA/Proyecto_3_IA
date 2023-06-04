#! /usr/bin/env python3

from py.read_files import get_data_files_content
from py.db_manipulation import split_list, split_columns
from py.utils import calculate_similarity_percentage, generate_table

from py.methods.KNN import KNN


def main():
    data = get_data_files_content()
    table_body = []

    for name in data:
        train, test = split_list(data[name])

        train_vals, train_labels = split_columns(train)
        test_vals, test_labels = split_columns(test)

        knn = KNN(train_vals, train_labels, test_vals)
        knn.generate_euclidean_distance_list()
        knn_predics = [
            knn.propose_prediction(k)
            for k in [1, 3, 5]
        ]
        knn_accuracy = [
            calculate_similarity_percentage(
                predic,
                test_labels
            )
            for predic in knn_predics
        ]

        table_body.append(
            [name] + knn_accuracy + [0.0]
        )

    generate_table(table_body)


if __name__ == '__main__':
    main()
