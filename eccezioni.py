def main():
    try:
        ore = int(input("Quante ore hai lavorato "))
        payrate = float(input("Inserisci la retribuzione oraria "))

    except ValueError: 
        print('Errore: Ore lavorate e retribuzione oraria devono')
        print('essere numeri validi')
    #except Exception as err: #err è una variabile a cui viene assagnato l'errore generico
        #print(err) #si stampa l'errore
    else: #viene eseguito solo se le eccezioni non ci sono
        grosspay = ore * payrate

        print("Paga lorda: ", grosspay)
    
    finally: #viene eseguito indipendentemente dalla presenza di eccezioni
             #ad esempio la chiusura di un file
        pass
        

main()