class X(object):
    attr = 100

    def __call__(self):
        return 'CALLED'


obj = X()

import pdb; pdb.set_trace()

pass
