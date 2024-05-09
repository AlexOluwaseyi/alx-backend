#!/usr/bin/env python3

"""
Create a class LFUCache  that inherits from BaseCaching
and is a caching system:

- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to
  call the parent init: super().__init__()
- def put(self, key, item):
  - Must assign to the dictionary self.cache_data the item
    value for the key key.
  - If key or item is None, this method should not do anything.
  - If the number of items in self.cache_data is higher
    that BaseCaching.MAX_ITEMS:
    - you must discard the least frequency used item (LFU algorithm)
    - if you find more than 1 item to discard, you must use the LRU
      algorithm to discard only the least recently used
    - you must print DISCARD: with the key discarded
      and following by a new line
- def get(self, key):
  - Must return the value in self.cache_data linked to key.
  - If key is None or if the key doesn’t exist in self.cache_data, return None
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class inherits cache_data from BaseCaching
    Implements puts and get method
    """
    def __init__(self):
        """
        Initializer
        Set up frequency counter for the cache which records
        each time the keys of the dict are referenced or used.
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)
        self.cache_freq = {}

    def put(self, key, item):
        """
        - def put(self, key, item):
          - Must assign to the dictionary self.cache_data the item
            value for the key key.
          - If key or item is None, this method should not do anything.
          - If the number of items in self.cache_data is higher
            that BaseCaching.MAX_ITEMS:
            - you must discard the least frequency used item (LFU algorithm)
            - if you find more than 1 item to discard, you must use the LRU
              algorithm to discard only the least recently used
            - you must print DISCARD: with the key discarded
              and following by a new line
        """
        if key is not None and item is not None:
            if key not in self.cache_data.keys():
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    sorts = sorted(self.cache_freq.items(),
                                   key=lambda item: item[1])
                    key_off = sorts[0][0]
                    del self.cache_data[key_off]
                    del self.cache_freq[key_off]
                    print(f'DISCARD: {key_off}')
                self.cache_data[key] = item
                self.cache_freq[key] = 1

            self.cache_data[key] = item
            self.cache_freq[key] += 1

    def get(self, key):
        """
        - def get(self, key):
            - Must return the value in self.cache_data linked to key.
            - If key is None or if the key doesn’t exist
              in self.cache_data, return None
            - Increments the freq for the key
        """
        try:
            self.cache_freq[key] += 1
            return self.cache_data[key]
        except KeyError:
            return None
