class MyIter(object):

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self, *args, **kwargs):
        return self

    def next(self):
        while self.iterable:
            return self.iterable.pop(0)
        raise StopIteration()


for i in iter([1,2,3]):
    print i


for i in MyIter([1,2,3]):
    print i
