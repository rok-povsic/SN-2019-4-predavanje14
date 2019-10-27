#import ddv
from ddv import izracun_ddv

cena = float(input("Vnesi ceno izdelka:"))
davek = izracun_ddv(cena)
print("DDV je: " + str(davek))
