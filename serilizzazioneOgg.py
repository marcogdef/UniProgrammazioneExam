#SERIALIZZAZIONE OGGETTI --- salvare un oggetto in un file
#serializzazione di un dizionario con nomi e numeri di telefono
import pickle #salva gli oggetti in python non leggibili come testo 

phonebook = {
'Mario': '555-1111',
'Giulia': '555-2222',
'Anna': '555-3333'
}

outputfile = open('phonebook.dat', 'wb') #apriamo un file in scrittura binaria dove inseriremo il  dizionario --- 'dat' file di tipo binario
pickle.dump(phonebook, outputfile) #serializza nel file il dizionario con la funzione dump del metodo pickle
outputfile.close()


#deserializzazione di un dizionario
inputfile = open('phonebook.dat', 'rb') #apriamo il file in lettura binaria
pb = pickle.load(inputfile) #si chiama la funzione load del metodo pickle per deseriallizare
print(pb) #stampo
inputfile.close()



#Programma che serializza un dizionario con informazioni personali
def main():
    again = 's'
    output_file = open('info.dat','wb')
    while again.lower() == 's':
        save_data(output_file)
        again = input('Vuoi inserire altri dati? (s/n): ')
    output_file.close()

def save_data(file):
    person = {}
    person['name'] = input('Nome: ') #crea delle coppie chiave:valore
    person['age'] = int(input('Età: '))
    person['weight'] = float(input('Peso: '))
    pickle.dump(person, file) #serializza i dati nel file 

main()


#Programma che deserializza un dizionario con informazioni personali
def main1():
    end_of_file = False
    input_file = open('info.dat', 'rb')
    while not end_of_file: #il ciclo non finisce fin quando non si arriva alla fine del file
        try:
            person = pickle.load(input_file) #deserializza il file assegnando tutti i dati (uno alla volta quindi ciclando) al dizionario person
            display_data(person) #passiamo alla funzione display_data il dizionario person
        except EOFError: #eccezione end of file per uscire dal ciclo
            end_of_file = True
    input_file.close()

def display_data(person):
    print('Nome:', person['name']) #dizionario['chiave a cui è assegnato un valore']
    print('Età:', person['age'])
    print('Peso:', person['weight'])

main1()