def printArgs(func):
    def innerFunc(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return innerFunc


@printArgs
def footbar(x,y,a,z,b):
    return x * y * z + a +b

print(footbar(3,5,6,z=10,b=15))