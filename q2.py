# det finns en lista med årtal
# [1952,1958,1962,1977,1980,1999]
# Skriv en loop som tar fram hur MÅNGA som är mellan 1950 och 1960
# skriv ut svaret

# jag fattar inte Stefan men
# jag antar att du menar exklusive

lista = [1952,1958,1962,1977,1980,1999]
antal = 0
for tal in lista:
    if tal > 1950 and tal < 1960:
        antal = antal + 1
print(antal)        

        


