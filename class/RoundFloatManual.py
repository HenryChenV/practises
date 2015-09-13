class RoundFloat(float):

    def __new__(self, value):
        assert isinstance(value, float), 'value must be float!'
        return super(RoundFloatManual, self).__new__(self, round(value, 2))

    def __str__(self):
        return '%.2f' % self


class RoundFloatManual(object):

    def __init__(self, value):
        assert isinstance(value, float), 'value must be float!'
        self.value = round(value, 2)

    def __str__(self):
        return '%.2f' % self.value

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    rfm = RoundFloatManual(4.2345)
    print rfm
