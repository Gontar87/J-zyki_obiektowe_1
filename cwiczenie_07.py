##7. Zaimplementuj dekorator, który wypisze nazwę i argumenty wywołanej funkcji.
from functools import wraps

def dekorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Nazwa funkcji: ' + func.__name__)
        for i, a in enumerate(args):
            print('Argument ' + str(i+1) +' = ' + str(a))

        
        for key, value in kwargs.items():
            print('{0}={1}'.format(key.value))

        return func(*args,**kwargs)
    return wrapper

@dekorator
def f(n):
    print(n)




    
      

    
    





