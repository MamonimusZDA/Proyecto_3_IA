#!/usr/bin/env python3

from dataclasses import dataclass
from collections import Counter

from ..db_manipulation import split_columns, merge_lists

import numpy as np


@dataclass
class KNN:
    train_vals: list
    train_labels: list
    test_vals: list

    def __calc_euclidean_distance(self, ln: list):
        tmp_ln = np.array(ln)
        dists = [float(
            np.sqrt(np.sum((ln - tmp_ln)**2))
        ) for ln in self.train_vals]
        return sorted(
            merge_lists(dists, self.train_labels),
            key=lambda x: x[0]
        )

    def generate_euclidean_distance_list(self):
        self.distances = [
            self.__calc_euclidean_distance(ln)
            for ln in self.test_vals
        ]

    def propose_prediction(self, k=5):
        predics = []
        for dist in self.distances:
            _, dists_label = split_columns(dist)
            counter = Counter(dists_label[:k])
            predic = max(
                counter, key=counter.get
            )
            predics.append(predic)
        return predics
