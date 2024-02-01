#!/usr/bin/env python3
"""
1. FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        a class that inherits from BaseCaching and is a caching system
        implementing a FIFO algorithm
        """
        if key and item:
            if key in self.keys:
                self.cache_data[key] = item
            else:
                if len(self.keys) > self.MAX_ITEMS - 1:
                    del self.cache_data[self.keys[0]]
                    print("DISCARD: {}".format(self.keys[0]))
                    self.keys = self.keys[1:]
                    self.keys.append(key)
                    self.cache_data[key] = item
                else:
                    self.keys.append(key)
                    self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.keys:
            return None
        return self.cache_data[key]
