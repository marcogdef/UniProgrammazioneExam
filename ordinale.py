def main():
    giorno1 = int(input('Inserisci il giorno: '))
    mese1 = int(input('Inserisci il mese: '))
    anno1 = int(input("Inserisci l'anno: "))
    giorno2 = int(input('Inserisci il giorno 2: '))
    mese1 = int(input('Inserisci il mese 2: '))
    anno2 = int(input("Inserisci l'anno 2: "))
    
    totalegiorni2 = g_mesi(mese1)
    totalegiorni2 += giorno1

    # Se l'anno è bisestile e il mese è dopo febbraio, aggiungi 1 giorno
    if bisestile(anno1) and mese1 > 2:
        totalegiorni2 += 1

    print(f"Il giorno {giorno1}/{mese1}/{anno1} è il {totalegiorni2}° dell'anno.")


def bisestile(anno):
    return (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0)


def g_mesi(mese):
    giorni_mese = [31,28,31,30,31,30,31,31,30,31,30,31]
    totalegiorni = 0
    for i in range(mese - 1):
        totalegiorni += giorni_mese[i]
    return totalegiorni




main()
