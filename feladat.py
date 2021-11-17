import random
list = ["Bea, Zoli, Dénes, Irén, Gáspár "]

nev = input('adj meg egy nevet: ')

if nev in list:
    print('benne van')
else:
    print("nincs benne")



szam1 = random.randint(10,30)
print