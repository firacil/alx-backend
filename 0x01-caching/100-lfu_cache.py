#!/usr/bin/env python3
"""
    LFU class BasicCache that inherits from BaseCaching and
    is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
        __summary__
    """

    def __init__(self):
        """
            __summary__
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = {}
        self.time = 0

    def put(self, key, item):
        """__summary__

            Args:
                key
                item
        """
        if key is None or item is None:
            return

        if key in self.cached_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                    k for k, v in self.frequency.items() if v == min_freq
                ]

                if len(least_freq_keys) > 1:
                    least_freq_keys.sort(key=lambda k: self.usage_order[k])
                key_to_evict = least_freq_keys[0]

                del self.cache_data[key_to_evict]
                del self.frequency[key_to_evict]
                del self.usage_order[key_to_evict]
                print("DISCARD: {:s}".format(key_to_evict))

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.usage_order[key] = self.time
        self.time += 1

    def get(self, key):
        """
            return the value in self.cache_data linked to key

            Args:
                key(__type__):_description_
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order[key] = self.time
        self.time += 1

        return self.cache_data[key]
