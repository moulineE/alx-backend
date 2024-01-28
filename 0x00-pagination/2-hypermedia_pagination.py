#!/usr/bin/env python3
"""
Simple pagination module
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int = 1, page_size: int = 10) -> Tuple[int, int]:
    """
    function index_range that takes two int args and return a tuple of size
    two containing a start index and an end index for the page
    :param page:
    :param page_size:
    :return: Tuple[start index, end index]
    """
    return (((page - 1) * page_size), (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        a method that takes two integer arguments and return a list
        :param page: INT
        :param page_size: INT
        :return: List[List]
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_indx, end_indx = index_range(page, page_size)
        data = self.dataset()
        length = len(data)
        if start_indx > end_indx or end_indx > length:
            return []
        return data[start_indx:end_indx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        a method
        :param page:
        :param page_size:
        :return:
        """
        data = self.get_page()
        start_indx, end_indx = index_range(page, page_size)
        data_base_size = len(self.__dataset)
        next_page = None
        prev_page = None
        if end_indx < data_base_size:
            next_page = page + 1
        if start_indx > 0:
            prev_page = page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": math.ceil(data_base_size/page_size)
        }
