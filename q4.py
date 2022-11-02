# I gymnastik får utövaren poäng(0-10) av ett antal domare. 
# Det lägsta och det högsta tas bort, sen blir resultatet för 
# utövaren SNITTET av de övrigas.
# Ett betyg är ett flyttal, dvs 9.5 är möjligt.
# Förutsätt att det alltid är 5 stycken domare. 
# Då matas 5 stycken resultat in och du beräknar poäng enligt formeln ovan,
# Och skriver ut såklart (3 decimaler tack :)   )! 
# Ex
# Poäng från domare 1: 9
# Poäng från domare 2: 4
# Poäng från domare 3: 5
# Poäng från domare 4: 5
# Poäng från domare 5: 7
# Resultat: 4,667
lista = []
while len(lista) < 5:
    nummer = len(lista)+1
    talet = float(input(f"Poäng från domare {nummer}:"))
    if talet >= 0 and talet <= 10:
        lista.append(talet)

storsta = max(lista)
minsta = min(lista)

summa = 0
for x in lista:
    summa = summa + x
snitt = summa / 5

summa = summa - minsta - storsta

snitt = summa / 3

print(f"Resultat:{snitt:.3f}")
