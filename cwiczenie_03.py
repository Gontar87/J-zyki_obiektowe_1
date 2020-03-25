
##3. Napisz funkcję, która usunie duplikaty z listy.
lista = [1,1,2,2,3,4,5,6,5]
print(lista)


def usun_duplikaty(lista):
    lista_wyjsciowa = []
    for i in lista:
       if i not in lista_wyjsciowa:
           lista_wyjsciowa.append(i)

    return lista_wyjsciowa

print (usun_duplikaty(lista))


     


    
      

    
    





