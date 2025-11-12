#PROGRAMMAZIONE PROCEDURALE E AD OGGETTI
import random

class Coin:
    def __init__(self): #init inizializza sideup a 'testa', chiamato convenzionalmente self: è il riferimento all'oggetto
        self.sideup = 'Testa' #attributo sideup che imposta il suo stato a 'testa'

    def toss(self):
        if random.randint(0,1) == 0: #funzione per assegnare al parametro self testa o croce random 
               self.sideup= 'Testa'
        else:
             self.sideup = 'Croce'
    
    def get_sideup(self): #funzione per restituire il valore di sideup all'oggetto (chiamato self)
        return self.sideup
    
#istanza o oggetto della classe coin
def main():
    mycoin = Coin() #con questa dicitura creiamo l'oggetto mycoin e viene gia eseguito il metodo init che inizializza il parametro self ovvero l'oggetto con 'testa'

    print('La faccia visibile è: ', mycoin.get_sideup()) #get_sideup è chiamato sull'oggetto mycoin e restituisce 'Testa', il parametro self fa automaticamente riferimento all'ogg mycoin
    print('Sto lanciando la moneta...')
    mycoin.toss() #funzione con la randint per determinare in maniera casuale la faccia della moneta
    print('La faccia visibile è:', mycoin.get_sideup()) #chiamata alla funzione che ritorna come parametro self dopo averlo randomizzato tramite la funzione toss


    mycoin2 = Coin() #abbiamo creato un secondo oggetto che avra anche lui come attributo sideup e parametro self ma sarà diverso da quelli di mycoin 
    print('La faccia visibile è: ', mycoin2.get_sideup())
    print('Sto lanciando la moneta...')
    mycoin2.toss()
    print('La faccia visibile è:', mycoin2.get_sideup())

main()





#attributi pubblici e privati
class Coin1:
     def __init__(self): #self è il parametro passato automaticamente alla funzione init, funge da riferimento all'oggetto mycoin3 quando si chiamano le funzioni
        self.sideup = 'Testa' #Attributo pubblico 
        self.__sideup = 'Testa' #__ rende l'attributo privato ovvero non puo essere acceduto dall'esterno

mycoin3 = Coin1()
mycoin3.sideup = 'Croce' #cambio lo stato dell'oggetto 
print(mycoin3.sideup) #output = Croce perche l'attributo è pubblico

#print(mycoin3.__sideup) #output = errore perche __sideup non puo essere acceduto dall'esterno della classe
    




#metodi accessori e mutatori (permettono di accedere ai dati di una classe, permettono di modificare gli attributi di una classe)

class Cellphone:
    def __init__(self, manufact, model, price): #passiamo gli attributi di un oggetto e gli inizializziamo
        self.__manufact = manufact #gli attributi esterni passati alla funzione vengono usati per inizializzare gli attributi interni e privati della classe
        self.__model = model
        self.__price = price

    # Metodi setter (mutatori)
    def set_manufact(self, manufact): #passiamo alla funzione l'oggetto(self) e l'attributo manufact
        self.__manufact = manufact #aggiorna il nome del produttore
    
    def set_model(self, model):
        self.__model = model #modifica il modello
    
    def set_retail_price(self, price):
        self.__price = price #aggiorna il prezzo di vendita

    # Metodi getter (accessori)
    def get_manufact(self): #restituisce il valore interno dell'attributo privato __manufact
        return self.__manufact
    
    def get_model(self): #restituisce il valore interno dell'attributo privato __model
        return self.__model
    
    def get_retail_price(self): #restituisce il valore interno dell'attributo privato __price
        return self.__price
    

#creazione oggetto
phone1 = Cellphone('Apple', 'Iphone 15', 999) #init viene eseguito quindi: self.__manufact = Apple, self.__model = Iphone 15, self.__price = 999

phone1.set_retail_price(600) #cosi aggiorniamo l'attributo privato self.__price senza accedervi direttamente
print(phone1.get_retail_price()) #cosi visualizziamo e stampiamo il valore aggiornato di self.__price