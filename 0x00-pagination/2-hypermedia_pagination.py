#!/usr/bin/env python3

"""
Server class to implement the index_range method
"""


import csv
import math
from typing import List, Any, Dict


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
        a method named get_page that takes two integer arguments page with
        default value 1 and page_size with default value 10.

        You have to use this CSV file (same as the one presented
          at the top of the project)
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
          correctly and return the appropriate page of the dataset
          i.e. the correct list of rows).
        If the input arguments are out of range for the dataset,
          an empty list should be returned.
        """
        data_list = []
        data_set = Server.dataset(self)
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        try:
            idx = index_range(page, page_size)
            for i in range(idx[0], idx[1]):
                data_list.append(data_set[i])
            return data_list
        except IndexError as e:
            return []


    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Implement a get_hyper method that takes the same
        arguments (and defaults) as get_page and returns
        a dictionary containing the following key-value pairs:

        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        Make sure to reuse get_page in your implementation.

        You can use the math module if necessary.
        """
        output_dict: Dict[str, Any] = {}
        output_dict['page_size'] = page_size
        output_dict['page'] = page
        output_dict['data'] = self.get_page(page, page_size)
        total_pages = math.ceil(len(Server.dataset(self)) / page_size)
        if page < total_pages:
            output_dict['next_page'] = page + 1
        else:
            output_dict['next_page'] = None
        if page == 1:
            output_dict['prev_page'] = None
        else:
            output_dict['prev_page'] = page - 1
        output_dict['total_pages'] = total_pages

        return output_dict



def index_range(page: int, page_size: int) -> tuple:
    """
    # Calculate start and end indices based on page number and page size
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
