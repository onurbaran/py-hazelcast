__author__ = 'onurbaran'

from hazelcast import MapApi


class Map(dict):

    def __init__(self, map_name):
        self.__map_name = map_name
        self.__hz = MapApi(self.__map_name)

    def add(self, key, value):
        self.__setitem__(key, value)
        return self.__hz.add(key, value)

    def get(self, key, d=None):
        value = self.__hz.get_item(key)
        if value is not None:
            self.__setitem__(key, value)
        return value

    def remove_all(self):
        self.clear()
        return self.__hz.clear()

    def remove(self, key):
        if key in self:
            self.__delitem__(key)
        return self.__hz.remove_key(key)

