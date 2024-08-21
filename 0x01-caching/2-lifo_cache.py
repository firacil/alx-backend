#!/usr/bin/env python3
"""
    class BasicCache that inherits from BaseCaching and
    is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
            return the value in self.cache_data linked to key

            Args:
                key(__type__):_description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
