#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function index_range that takes two int args and return a tuple of size
    two containing a start index and an end index for the page
    :param page:
    :param page_size:
    :return: Tuple[start index, end index]
    """
    return (((page - 1) * page_size), (page * page_size))
