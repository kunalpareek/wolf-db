from abc import ABC

class Storage(ABC):
    '''
    Key Value store base class
    '''
    def get(self, key):
        '''
        '''
        raise NotImplementedError

    def delete(self, key):
        '''
        '''
        raise NotImplementedError

    def put(self, key, value):
        '''
        '''
        raise NotImplementedError

