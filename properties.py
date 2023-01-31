
class propertyClass:

    def __init__(self, data):
        self._data = data

    @property
    def prop(self):
        return self._data

    @prop.setter
    def prop(self, value):
        self._data = value


if __name__ == '__main__':
    c = propertyClass('test')
    print(c.prop)
    c.prop = 0
    print(c.prop)
