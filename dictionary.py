class Dictionary:

    def __init__(self, items):

        if type(items) != list:
            raise ValueError('this is not a list')
        else:
            for i in range(len(items)):
                if type(items[i]) != tuple:
                    raise ValueError('key/value pairs must be given as a list of 2-length tuples')
                elif len(items[i]) > 2:
                    raise ValueError('all key/value pairs must be given as a list of 2-length tuples')

        self.__keys = []
        self.__values = []
        self.__items = items

        for i in range(len(items)):
            self.__keys.append(items[i][0])
            self.__values.append(items[i][1])

    def keys(self):
        return self.__keys

    def values(self):
        return self.__values

    def items(self):
        return self.__items

    def valueForKey(self, key):
        keyIndex = self.__keys.index(key)
        return self.__values[keyIndex]

    def appendNew(self, new):
        if type(new) != list:
            raise ValueError('this is not a list')
        else:
            if len(new) > 2:
                raise ValueError('all key/value pairs must be given as a list of 2-length tuples')

        mytuple = (new[0], new[1])
        self.__items.append(mytuple)
        self.__keys.clear()
        self.__values.clear()
        for i in range(len(self.__items)):
            self.__keys.append(self.__items[i][0])
            self.__values.append(self.__items[i][1])
        
