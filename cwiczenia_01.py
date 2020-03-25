print ("Podaj szerokość pokoju: " )
szerokosc = input()
print ("Podaj długość pokoju: " )
dlugosc = input()
sciana = '*'
sciana2 = '|'


for i in range (0,int(szerokosc)):
    sciana = sciana + ' - '
    sciana2 = sciana2 + ' . '
sciana = sciana + '*'
sciana2 = sciana2 + '|'


print(sciana)
for i in range (0,int(dlugosc)):
    print(sciana2)
print(sciana)


