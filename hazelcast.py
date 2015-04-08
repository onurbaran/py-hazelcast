__author__ = 'onurbaran'

import requests


class BaseApi(object):

    CACHE_ENDPOINT = "http://127.0.0.1:5701/hazelcast/rest/"
    CLUSTER_URI = "cluster"

    def __init__(self, object_type):
        self._object_type = object_type

    def call(self, key, **kwargs):
        pass

    def post(self, url, data):
        try:
            response = requests.post(url, data=data)
            return self._check_by_status_code(response.status_code)
        except Exception as e:
            # @TODO: log e.message & rollback & commit etc
            print e.message
            return False

    def get(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
            else:
                return None
        except Exception as e:
            print e.message
            raise Exception("Key Error")

    def delete(self, url):
        try:
            response = requests.delete(url)
            return self._check_by_status_code(response.status_code)
        except Exception as e:
            # @TODO: log e.message & rollback & commit etc
            print e.message
            return False

    def get_cluster_status(self, **kwargs):
        """ get hazelcast cluster status """
        url = "%s%s" % (self.CACHE_ENDPOINT, self.CLUSTER_URI)
        response = requests.get(url)
        return self._check_by_status_code(response.status_code)

    def _get_api_url(self, object_name, **kwargs):
        if 'key' in kwargs:
            return "%s%s/%s/%s" % (self.CACHE_ENDPOINT, self._object_type, object_name, kwargs['key'])
        else:
            return "%s%s/%s" % (self.CACHE_ENDPOINT, self._object_type, object_name)

    def _check_by_status_code(self, status_code):
        if status_code == 200:
            return True
        else:
            return False


class MapApi():

    def __init__(self, namespace):
        self.hazelcast = BaseApi("maps")
        self.__namespace = namespace

    def add(self, key, value):
        url = self.hazelcast._get_api_url(self.__namespace, key=key)
        return self.hazelcast.post(url, value)

    def get_item(self, key):
        url = self.hazelcast._get_api_url(self.__namespace, key=key)
        return self.hazelcast.get(url)

    def remove_key(self, key):
        url = self.hazelcast._get_api_url(self.__namespace, key=key)
        return self.hazelcast.delete(url)

    def clear(self):
        url = self.hazelcast._get_api_url(self.__namespace)
        return self.hazelcast.delete(url)

