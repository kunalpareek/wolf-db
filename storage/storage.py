from . import Storage

class InMemoryStorage(Storage):
    '''
    In memory kv store
    '''
    def __init__(self):
        self.data_store = {}

    def get(self, key):
        '''
        '''
        try:
            value = self.data_store[key]
        except KeyError:
            return None

    def put(self, key, value):
        '''
        '''
        self.data_store[key] = value
        return True

if __name__ == "__main__":
    kvs = InMemoryStorage()
    print(kvs.put("abc", 123))
    print(kvs.get("ab"))