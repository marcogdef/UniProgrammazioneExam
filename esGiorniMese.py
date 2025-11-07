def main():
    giorni_mese = ['31','28','31','30','31','30','31','31','30','31','30','31']
    mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']

    month = input('Di quale mese vuoi sapere il numero di giorni? ')

    if month in mesi:
        meseIndex = mesi.index(month) #troviamo l'indice del mese inserito
        numDays = giorni_mese[meseIndex]
        print(f'{month} è formato da {numDays} giorni')

    else:
        print(f'{month} non è un mese esistente')

main()


#RISOLVIBILE NELLA METà DELLE RIGHE PERO VABBE