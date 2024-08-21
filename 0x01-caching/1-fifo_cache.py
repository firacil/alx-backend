#!/usr/bin/env python3
"""
    class BasicCache that inherits from BaseCaching and
    is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        __summary__
    """

    def __init__(self):
        """
            __summary__
        """
        super().__init__()

    def put(self, key, item):
        """__summary__

            Args:
                key
                item
        """
        if key is None or item is None:
            pass

        # if the key already exists, update it and move it to end
        if key in self.cache_data:
            self.cache_data.pop(key)

        # adding the key-value pair to cache
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)

    def get(self, key):
        """
            return the value in self.cache_data linked to key

            Args:
                key(__type__):_description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
