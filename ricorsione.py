#RICORSIONE
def main(): #esempio di funzione ricorsiva infinita, ripeterà il messaggio infinite volte
    message()

def message():
    print('Cacca')
    
    message()

#main()

#=====================================

#implementazione di una condizione di arresto
def main1():
    message1(5) #passiamo alla funzione il parametro 5 che permetterà di visualizzare il messaggio 5 volte

def message1(times):
    if times > 0:
        print('Questa è una funzione ricorsiva')

        message1(times -1) #si richiama la funzione riducendo il problema a ogni passo fino ad arrivare a 0

main1()