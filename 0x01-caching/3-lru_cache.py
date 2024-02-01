#!/usr/bin/env python3
"""
3. LRU Caching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.keys = {}
        self.LRU_nb = 0

    def put(self, key, item):
        """
        a class that inherits from BaseCaching and is a caching system
        implementing a FIFO algorithm
        """
        if key and item:
            if key in self.keys.keys():
                self.cache_data[key] = item
                self.keys[key] = self.LRU_nb
                self.LRU_nb += 1
            else:
                if len(self.keys) >= self.MAX_ITEMS:
                    del_key = min(self.keys, key=self.keys.get)
                    del self.cache_data[del_key]
                    print("DISCARD: {}".format(del_key))
                    del self.keys[del_key]
                    self.cache_data[key] = item
                    self.keys[key] = self.LRU_nb
                    self.LRU_nb += 1
                else:
                    self.keys[key] = self.LRU_nb
                    self.LRU_nb += 1
                    self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.keys.keys():
            return None
        self.keys[key] = self.LRU_nb
        self.LRU_nb += 1
        return self.cache_data[key]
