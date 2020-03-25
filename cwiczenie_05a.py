##5. Napisz funkcję, która przefiltruje listę liczb całkowitych w celu znalezienia liczb
##pierwszych. Wykorzystaj w tym celu:
##a. funkcje map i filter
##b. list comprehension


def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


liczbyCalkowite = list(range(100))


liczbyPierwsze1 = list(filter(lambda x:is_prime(x), liczbyCalkowite))
liczbyPierwszeTreuFalse = list(map(lambda x:is_prime(x), liczbyCalkowite))
liczbyPierwsze2 = []

for i, el in enumerate(liczbyPierwszeTreuFalse):
    if liczbyPierwszeTreuFalse[i]:
        liczbyPierwsze2.append(liczbyCalkowite[i])
        

print(liczbyPierwsze1)
print('####')
print(liczbyPierwsze2)








     


    
      

    
    





