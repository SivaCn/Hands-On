

def restrict(func):
    def wraps(user):
        print 'pre processing'
        if user.lower() == 'john':
            func(user)
        else:
            print 'NOT AUTHORIZED'
        print 'post processing'

    return wraps


class cdec(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, user):
        print 'pre processing'
        if user.lower() == 'john':
            self.func(user)
        else:
            print 'NOT AUTHORIZED'
        print 'post processing'


#@restrict

@cdec
def method(user):
    print 'Actual method'


method('John')
method('John miller')
