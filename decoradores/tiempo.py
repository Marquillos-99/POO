"""
#import time

#def timer(funcion):
  def wrapper(*args, **kwargs):
    start = time.time()
    funcion(*args, **kwargs)
    end = time.time()
    print(f"Tiempo de ejecución: {end - start} segundos")
  return wrapper

#@timer
#def fibonacci(n):
#  if n <= 1:
#    return n
#  else:
    return fibonacci(n-1) + fibonacci(n-2)

#fibonacci(35)
"""
class MyDec(object):
    def __init__(self,flags):
        self.flags = flags

    def __call__(self, original_func):
        decorator_self = self
        def wrapper(*args, **kwargs):
            print("en decorator antes del wrapper", decorator_self.flags)
            original_func(*args, **kwargs)
            print("en decorator despues del wrappe", decorator_self.flags)
        return wrapper
    
@MyDec(flags="foo de fa fa")
def  bar(a,b,c):
    print("En bar(...) :", a, b, c)

if __name__ == "__main__":
    bar(1, "Hola", True)