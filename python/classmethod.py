"""Using @classmethod decorator as a way of 'constructor overloading'."""


class DataManager(object):

    def __init__(self, data_sequence):
        """Init expects a sequence."""
        self.data = " ".join(data_sequence)

    @classmethod
    def init_from_dict(cls, data_dict):
        return cls(data_dict.values())

    @classmethod
    def init_from_file(cls, filepath):
        with open(filepath, 'r') as f:
            data = f.readlines()
        return cls(data)


# DataManager objects 'instantiated' with different data
print DataManager(['a', 'b', 'c']).data
print DataManager.init_from_dict({1: 'd', 2: 'e', 3: 'f'}).data
print DataManager.init_from_file('/tmp/data').data
