def gen(inp):
    for i in inp:
        yield i


for i in gen(range(3)):
    print i

