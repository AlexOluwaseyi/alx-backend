#!/usr/bin/env python3

"""
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:

- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to
  call the parent init: super().__init__()
- def put(self, key, item):
  - Must assign to the dictionary self.cache_data the
    item value for the key key.
  - If key or item is None, this method should not do anything.
  - If the number of items in self.cache_data is higher
    that BaseCaching.MAX_ITEMS:
    - you must discard the first item put in cache (FIFO algorithm)
    - you must print DISCARD: with the key discarded
      and following by a new line
- def get(self, key):
  - Must return the value in self.cache_data linked to key.
  - If key is None or if the key doesn’t exist
    in self.cache_data, return None.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherits cache_data from BaseCaching
    Implements puts and get method
    """
    def __init__(self):
        # super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        - def put(self, key, item):
            - Must assign to the dictionary self.cache_data the
                item value for the key key.
            - If key or item is None, this method should not do anything.
            - If the number of items in self.cache_data is higher
                that BaseCaching.MAX_ITEMS:
                - you must discard the first item put in cache (FIFO algorithm)
                - you must print DISCARD: with the key discarded
                and following by a new line
        """
        # print(f'Current dict: {self.cache_data}')
        if key is not None and item is not None:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                for keys in self.cache_data.keys():
                    print(f'DISCARD: {keys}')
                    del self.cache_data[keys]
                    break
            self.cache_data[key] = item

    def get(self, key):
        """
        - def get(self, key):
            - Must return the value in self.cache_data linked to key.
            - If key is None or if the key doesn’t exist
                in self.cache_data, return None.
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None

