#!/usr/bin/env python3
"""
    class BasicCache that inherits from BaseCaching and
    is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        __summary__
    """

    def __init__(self):
        """
            __summary__
        """
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """__summary__

            Args:
                key
                item
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))

        if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
            remove = self.usedKeys.pop(0)
            del self.cache_data[remove]
            print("DISCARD: {:s}".format(remove))

    def get(self, key):
        """
            return the value in self.cache_data linked to key

            Args:
                key(__type__):_description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
