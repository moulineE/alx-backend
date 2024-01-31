#!/usr/bin/env python3
"""
Task 0. Basic dictionary module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a class that inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        """assign to the cache dictionary item value for the key key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
