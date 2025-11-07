import programmOggClassi #importiamo programmOggClassi cosi da utilizzare la classe Cellphone
import pickle #importiamo pickle per de/serializzare le istanze di classi 

FILENAME = 'cellphones.dat' 

#serializzazione
def main():
    again = 's'
    output_file = open(FILENAME, 'wb')

    while again.lower() == 's':
        man = input('Inserisci il produttore: ')
        mod = input('Inserisci il modello: ')
        retail = float(input('Inserisci il prezzo di vendita: '))

        phone = programmOggClassi.Cellphone(man, mod, retail) #creiamo l'oggetto phone e passiamo a Cellphone man, mod, retail

        pickle.dump(phone, output_file) #inseriamo i dati di phone nel file 
        again = input('Vuoi inserire altri dati? s/n: ')
    output_file.close()
main()

#deserializzazione e passaggio a funzione di un oggetto
def main2():
    end_of_line = False
    input_file = open(FILENAME, 'rb')

    while not end_of_line: #fin tanto che non è la fine del file 
        try:
            phone = pickle.load(input_file) #carichiamo un oggetto di Cellphone inserito precedentemente nel file output_file e lo assegna a phone, se abbiamo piu di un oggetto ne fa uno alla volta e ne stampa i dati
            display_data(phone) #stampa a video i dati dell'istanza
        except EOFError:
            end_of_line = True
    input_file.close

def display_data(phone): #stampa i dati di quell'oggetto che viene assegnato a phone in un ciclo del while
    print(f'Produttore: {phone.get_manufact()}')
    print(f'Numero di modello: {phone.get_model()}')
    print(f'Prezzo di vendita: €{phone.get_retail_price():,.2f}') 

main2()