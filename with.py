

class UseWith(object):
    def __init__(self):
        pass

    def __enter__(self, *args, **kwargs):
        pass
        print 'Enter'
        # create session

    def __exit__(self, *args, **kwargs):
        print 'Exit'
        # commit / rollback session
        # close session



with UseWith() as alias:
    #
    print 'inside'
    #

