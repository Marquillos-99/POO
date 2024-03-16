def decorator(func):
    print ("Soy el decorator")
    return func

@decorator
def Hello():
    print ("Soy el Hello")


@decorator
def Name():
    print ("Soy el Name")

Hello()

Name()