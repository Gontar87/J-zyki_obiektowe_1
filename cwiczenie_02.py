
##2. Przećwicz operację slice’a na listach:
##a. wypisz co trzeci element listy rozpoczynając od 3. elementu,
##b. odwróć listę,
##c. wypisz co drugi element od końca zaczynając od przedostatniego elementu, a
##kończąc na drugim.
lista = []

for i in range (1,101):
    lista.append(i)

a = slice(3,100,3)
print(lista[a])

lista_odwrocona = []    

for i in reversed(lista):
    lista_odwrocona.append(i)

print(lista_odwrocona)

b = slice(-1,-100,-2)
print(lista[b])


    
      

    
    





