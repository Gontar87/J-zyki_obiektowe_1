##8.Zaimplementuj dekorator, który zliczy i wypisze na standardowe wyjście liczbę
##wywołań danej funkcji
from functools import wraps



def dekorator(func):
    def licznik(x):
        licznik.calls += 1
        print('Liczba wywolań funkcji "' + func.__name__ + '" : ' + str(licznik.calls))
        return func(x)
    licznik.calls = 0

    return licznik

@dekorator
def funkcja(x):
    print(x)


for i in range(10):
    funkcja(i)







    
      

    
    





