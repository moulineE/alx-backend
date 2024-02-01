#!/usr/bin/env python3
"""
2. LIFO Caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
                index = self.keys.index(key)
                self.cache_data[key] = item
                del self.keys[index]
                self.keys.append(key)
                print(self.keys)
            else:
                if len(self.keys) > self.MAX_ITEMS - 1:
                    del self.cache_data[self.keys[-1]]
                    print("DISCARD: {}".format(self.keys[-1]))
                    self.keys = self.keys[:-1]
                    self.keys.append(key)
                    self.cache_data[key] = item
                    print(self.keys)
                else:
                    self.keys.append(key)
                    self.cache_data[key] = item
                    print(self.keys)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.keys:
            return None
        return self.cache_data[key]
