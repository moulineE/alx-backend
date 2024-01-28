# Project 0x00. Pagination

## Description
This project focuses on implementing pagination functionality for a dataset using Python. The primary goal is to understand and implement various techniques for paginating data, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Learning Objectives
Upon completion of this project, you should be able to explain the following concepts without the help of external sources:

- How to paginate a dataset with simple page and page_size parameters.
- How to paginate a dataset with hypermedia metadata.
- How to paginate in a deletion-resilient manner.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should follow the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation (run `python3 -c 'print(__import__("my_module").__doc__)'`).
- All functions should have documentation (run `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (length will be verified).
- All functions and coroutines must be type-annotated.

### Setup: Popular_Baby_Names.csv
Use the provided data file (`Popular_Baby_Names.csv`) for your project.

## Tasks

### Task 0: Simple Helper Function
Write a function named `index_range` that takes two integer arguments: `page` and `page_size`. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Example:
```python
res = index_range(1, 7)
print(type(res))
print(res)
# Output: (<class 'tuple'>, (0, 7))
```

### Task 1: Simple Pagination
Copy the `index_range` function from the previous task and implement a `get_page` method in the `Server` class. The `get_page` method should use the `index_range` to find the correct indexes to paginate the dataset and return the appropriate page of the dataset. If the input arguments are out of range for the dataset, an empty list should be returned.

Example:
```python
server = Server()
print(server.get_page(1, 3))
# Output: [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'],
#          ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'],
#          ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
```

### Task 2: Hypermedia Pagination
Replicate code from the previous task and implement a `get_hyper` method that returns a dictionary containing hypermedia metadata, including page_size, page number, dataset page, next page, previous page, and total pages.

Example:
```python
server = Server()
print(server.get_hyper(1, 2))
# Output: {'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'],
#                                               ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']],
#          'next_page': 2, 'prev_page': None, 'total_pages': 9709}
```

### Task 3: Deletion-Resilient Hypermedia Pagination
Implement a `get_hyper_index` method that returns a dictionary with hypermedia metadata and considers deletion-resilience. The method should take two integer arguments: `index` with a None default value and `page_size` with a default value of 10.

Example:
```python
server = Server()
print(server.get_hyper_index(3, 2))
# Output: {'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'],
#                               ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']],
#          'page_size': 2, 'next_index': 5}
```

## Author
Emmanuel Turlay, Staff Software Engineer at Cruise