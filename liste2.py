#LE LISTE2

lista1 = [1,2,3,4,5]
lista2 = lista1

print(lista1)
print(lista2)

lista1[0] = 99

print(lista1)
print(lista2) #list1 e list2 sono la stessa cosa, infatti dopo aver modificato 
              #l'indice 0 entrambe risulteranno con 99

print('')





#copia di liste

lista3 = [1,2,3,4]
lista4 = [] #creazione lista vuota

for item in lista3:
    lista4.append(item) #metodo append copia il contenuto di lista3 in quello di lista4 rendendole identiche ma separate
print(lista4)

print('')




#altro metodo per duplicare una lista

lista5 = [1,2,3,4,5]
lista6 = [] + lista5
print(lista6)

print('')





#calcolare la somma e la media dei valori in una lista

scores  = [5,7,8.9,9,1]

total = 0.0 #'total' funge da accumulatore
for voto in scores:
    total +=voto

print("La somma dei voti corrisponde a ", total)
media = total / len(scores)
print("La media dei voti è ", media)


print('')




#modulo random: la funzione choice

import random
names = ['cazzi', 'stracazzi', 'ultracazzi']
winner = random.choice(names) #choice restituisce uno o piu elementi a caso nella lista 
print(winner)

#choices
numeri = [1,2,3,4,5,6,7,8,9]
selected = random.choices(numeri, k=3) #k=3 serve ad indicare quanti elementi casuali estrarre (gli elementi possono essere ripetitivi)
print(selected)


print('')





#modulo random: la funzione sample (diversa da choises perchè non puo ripetere gli elementi)
numbers = [1,2,3,4,5,6,7]
sel = random.sample(numbers, k=3)
print(sel)

print("")





#passaggio di una lista ad una funzione

def get_total(value_list):
    # Crea una variabile da usare come accumulatore.
    totale = 0
    # Calcola il totale degli elementi della lista.
    for num in value_list:
        totale += num

    # Restituisce il totale.
    return totale

def main():
    # Crea una lista.
    numberss = [2, 4, 6, 8, 10]

    # Visualizza il totale degli elementi della lista.
    print(f'Il totale è {get_total(numberss)}')

print("")




#restituzione di una lista da una funzione
def getValues():
    values = []
    again = 's'

    while again == 's':
        num = int(input('Inserisci un numero: '))
        values.append(num) #aggiunge il numero inserito alla lista
        print('Vuoi aggiungere un numero?')
        again = input('s = si, qualsiasi altra cosa = no: ')
        print()
    
    return values

def main2():
    numm = getValues() #ottiene la lista values

    print('I numeri contenuti nella lista sono: ')
    print(numm)

print('')





#scritture di liste su file con writelines

cities = ['Newyork', 'Madrid', 'Atlanta']

outfile = open('cities.txt', 'w')

outfile.writelines(cities) #non aggiunge \n automaticamente

outfile.close()

#scritture di liste su file con ciclo for
outfile = open('cities.txt', 'w')
for item in cities:
    outfile.write(item +'\n') #con \n le città vengono scritte su caratteri di nuove righe

outfile.close()


print('')




#lettura di liste da file con readlines

infile = open('cities.txt', 'r')

cities = infile.readlines() # Legge il contenuto del file e lo memorizza in una lista.

infile.close() 

for index in range(len(cities)):
    cities[index] = cities[index].rstrip('\n') # Elimina \n da ogni elemento.

print('')





#scrittura di liste numeriche con ciclo for

listaN = [1,2,3,4,5,6,7,8,9,10]
nFileW = open('numberlist.txt', 'w')

for item in listaN:
    nFileW.write(str(item)+'\n')

nFileW.close()

print()




#lettura di liste numeriche con ciclo for
nFileR = open('numberlist.txt', 'r')

nummm = nFileR.readlines() #legge il contenuto del file e lo memorizza in una lista

nFileR.close()

for index in range(len(nummm)):
    nummm[index] = int(nummm[index]) #converte ogni elemento in int







