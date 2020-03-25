##6. Napisz generator kolejnych liczb Fibonacciego.

def fibonacci(a):
    n = int(a)
    p = 0
    q = 1
    s = 1
    if n == 1:
        print(p)
    elif n > 1:
        print(p)
        print(q)
        for l in range(3,n+1):
          print(s)
          b = s + q
          q = s
          s = b
    else:
        print('Niepoprawne dane wejściowe')
          
print('Podaj długość ciagu Fibonacciego:')           
n = input()
fibonacci(n)


     


    
      

    
    





