def ponavljajoc_input_za_stevilko():
    while True:
        try:
            stevilka = int(input("Vnesi:"))
            return stevilka
        except:
            print("Nisi vnesel stevilke")


stevilka1 = ponavljajoc_input_za_stevilko()
stevilka2 = ponavljajoc_input_za_stevilko()

# Preprican, da sta stevilka1 in stevilka2 res stevilki.
print("Vnesel si " + str(stevilka1) + " " + str(stevilka2))
