#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """
        method that return a dict
        :param index:
        :param page_size:
        :return:
        """
        data = []
        index_dataset = self.indexed_dataset()
        sorted_index = sorted(index_dataset.keys())
        last = sorted_index[-1]
        if index is None:
            index = 0
        assert index >= 0 and index <= last
        x = page_size
        i = 0
        while i < x:
            try:
                data.append(index_dataset[index + i])
                i += 1
            except Exception:
                x += 1
                i += 1
                continue
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": (index + x)
        }
