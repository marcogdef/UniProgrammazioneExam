accumulatore = 0
somma = 0
voto1 = int(input("Inserisci voto "))
while voto1<0 or voto1>30:
    print("voto non valido ")
    voto1 = int(input("Riscrivilo "))


voto2 = 0
while voto2>=0 and voto2<=30:
    somma = somma + voto2
    accumulatore = accumulatore + 1
    voto2 = int(input("Riscrivi un altro numero o digita +30 per uscire "))

somma = somma + voto1
print(accumulatore)
print(float(somma)/accumulatore)