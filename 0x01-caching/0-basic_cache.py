#!/usr/bin/env python3
"""
    class BasicCache that inherits from BaseCaching and
    is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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
