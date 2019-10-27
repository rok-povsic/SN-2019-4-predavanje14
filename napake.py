stevilka = int(input("Vnesi stevilko: "))

try:
    obratna_stevilka = 1 / stevilka
    print("Obratna stevilka je: " + str(obratna_stevilka))
except:
    print("Prislo je do napake")


seznam = []
while True:
    try:
        seznam.append(1 / int(input("Vpisi stevilo: ")))
    except:
        print("Nisi vpisal stevilke")
        break

print(seznam)
