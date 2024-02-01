#!/usr/bin/env python3
"""
5. LFU Caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()
        self.keys = {}
        self.LRU_nb = 0

    def put(self, key, item):
        """
        a class that inherits from BaseCaching and is a caching system
        implementing a LFU algorithm
        """
        if key and item:
            if key in self.keys.keys():
                self.cache_data[key] = item
                self.keys[key]['LRU_nb'] = self.LRU_nb
                self.keys[key]['LFU_nb'] += 1
                self.LRU_nb += 1
            else:
                if len(self.keys) >= self.MAX_ITEMS:
                    min_value = min(self.keys[key]['LFU_nb']
                                    for key in self.keys)
                    del_key = min(self.keys,
                                  key=lambda x: (self.keys[x]['LFU_nb'],
                                                 self.keys[x]['LRU_nb'])
                                  if self.keys[x]['LFU_nb'] == min_value
                                  else (float('inf'), float('inf')))
                    del self.cache_data[del_key]
                    print("DISCARD: {}".format(del_key))
                    del self.keys[del_key]
                self.cache_data[key] = item
                self.keys[key] = {'LRU_nb': self.LRU_nb, 'LFU_nb': 0}
                self.LRU_nb += 1

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.keys.keys():
            return None
        self.keys[key]['LRU_nb'] = self.LRU_nb
        self.keys[key]['LFU_nb'] = self.keys[key]['LFU_nb'] + 1
        self.LRU_nb += 1
        return self.cache_data[key]
