class MyList():
    def __init__(self, l1):
        self.l1 = l1

    def __add__(self, l2):
        for i in l2.l1:
            self.l1.append(i)
        return self.l1


import pdb; pdb.set_trace() ## XXX: Remove Thi

obj1 = MyList([1,2,3])
obj2 = MyList([4, 5,6])
obj3 = MyList([4, 5,6])
obj4 = MyList([4, 5,6])
obj5 = MyList([4, 5,6])
obj6 = MyList([4, 5,6])


accum = MyList([])
for obj in ( obj1, obj2, obj3, obj4, obj5, obj6,):
    accum + obj

print accum.l1
