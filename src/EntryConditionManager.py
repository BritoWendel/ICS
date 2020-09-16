class EntryConditionManager(object):
    def __init__(self, size):
        self.__size = size
        self.__list = []
        pass

    def add(self, condition):
        self.__list.append(condition)

    def iterate(self, entry):
        text = entry.get()

        for i in self.__list:
            if len(text) == i.pos:
                entry.insert(i.symbol)
            elif len(text) != i.pos+1:
                if text[-1] == i.symbol:
                    entry.set(text[:-1])

        if len(text) > self.__size:
            entry.set(text[:self.__size])

