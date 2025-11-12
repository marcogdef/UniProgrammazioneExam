#DIZIONARI - coppie chiave-valore 

phonebook = {
    'mario': '555-111', #coppia chiave:valore -- mario è la chiave
    'giulia': '666-333', #le chiavi sono oggetti immutabili 
    'claudia': '777-888' #gli oggetti del dizionario non sono ordinati
}

#operatore IN nei dizionari
if 'mario' in phonebook:
    print(phonebook['mario'])
if 'anna' not in phonebook:
    print('Anna non è in phonebook') 



#operazioni sui dizionari
#metodi sui dizionari
#clear, get, items, keys, pop, popitem, values

#metodo get
value = phonebook.get( #se claudia è contenuta in phonebook value avrà come valore 777-888, se non lo è value = 'la voce ecc...'
    'claudia',
    'La voce non è stata trovata'
)
print(value)


#metodo items
for key,valore in phonebook.items(): #genera una tupla con due valori key,valore associati a ogni oggett chiave:valore
    print(key,valore)


#metodo keys
for chiave in phonebook.keys(): #keys ritorna solo la chiave
    print(chiave)


#metodo pop
phone_num = phonebook.pop( #se claudia si trova in phonebook la rimuove
    'claudia',
    'non è stata trovata'
)


#metodod popitem
key2, value2 = phonebook.popitem() #popitem rimuove e restituisce l'ultima coppia del dizionario
print(key2,value2)


#metodo values
for val in phonebook.values(): #restituisce tutti i valori del dizionario 
    print(val)


#metodo clear
phonebook.clear() #clear restituisce il dizionarioi vuoto




#AGGIUNGERE O AGGIORNARE ELEMENTI AD UN DIZIONARIO
phonebook['Rosanna'] = '774-899' #ho aggiunto un valore a phonebook
phonebook['Pierino'] = '774-898'
phonebook['claudia'] = '888-111' #ho aggiornato il valore alla chiave claudia in phonebook


#ELIMINARE ELEMENTI DA UN DIZIONARIOù
del phonebook['claudia'] #elimino la coppia chiave 'claudia'


#DETERMINARE NUMERO DI ELEMENTI IN UN DIZIONARIO

num_items = len(phonebook) #tramite operatore LEN
print(num_items)



#VALORI COME LISTE
testscores = {
    'kayla': [26,56,78],
    'bimbi': [72,54,89],
    'sium': [22,45,23]
}

kayla_scores = testscores['kayla']
print(kayla_scores)


#CHIAVI E VALORI MISTI
mix = {'ABC': 1, 99: 'YABABA', (7,9,2):[8,5,6]}


#DIZIONARI VUOTI
sas = {}
sas['pierino'] = '3452' #aggiungo elementi al dizionario



#ITERAZIONE DEI DIZIONARI CON FOR
for key in phonebook:
    print(key) #stampa solo le chiavi

for key in phonebook: 
    print(key, phonebook[key]) #stampa le coppie chiave:valore
