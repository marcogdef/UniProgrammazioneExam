#LE LISTE

lista2 = [1,3,'ciaoo',7]    
for i in lista2:
    print(i)

print("")



lista = list(range(5))
for i in lista:
    print(i)

print("")



mylist = [10,20,30,40]
index = 0 #index fa riferimento all'indice della lista es. index = 0 si riferirà al valore 10 nella lista
while index < 4: #o index < len(mylist)
    print(mylist[index]) 
    index+=1

print("")




#modifica valori lista 
number = [1,2,3,4,5]

print(number)

number[0] = 99 #[0] indica il primo indice della lista 

print(number)

print("")





#assegnazione valori a lista
numbers = [0] * 5
for index in range(len(numbers)):
    numbers[index] = 99 #assegna a ogni indice della lista il valore 99

print("")





#concatenazione di liste
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = list1 + list2 #or list1 += list2
print(list3)   

print("")




#slicing nelle liste
days = [1,2,3,4,5,6,7] #vogliamo stampare solo i numeri centrali quindi 3,4,5
print(days[2:5]) #i valori nelle parentesi fanno riferimento sempre agli indici, ultimo valore sempre escluso quindi 5-1 = 4
                 #potremmo anche inserire solo il valore finale quindi [:3] oppure solo valore iniziale quindi es. [2:]

print("")


#slicing nelle liste con step
num = [1,2,3,4,5,6,7,8,9,10] 
print(num[1:10:2])

print("")



#slicing negativo nelle liste
num1 = [1,2,3,4,5,6,7,8,9,10] 
print(num1[-5:]) #numero 10 = [-1] numero 9 = [-2] ecc numero 6 = [-5] 

print("")





#ricerca nelle liste
def main():
    prodotti = ['patate', 'cipolle', 'anguria', 'melone']

    cerca = input('Inserisci il nome del prodotto: ')

    if cerca in prodotti: # l'operatore in controlla se la variabile 'cerca' data dall'utente si trova nella lista 'prodotti'
        print(f'{cerca} è stato trovato nella lista')
    else:
        print(f'{cerca} non è stato trovato nella lista')

    #ESISTE ANCHE L'OPERATORE 'NOT IN' OVVERO IL CONTRARIO
main()


print("")





#metodi nelle liste
#metodo append -  per aggiungere ad una lista un valore all'ultimo posto

nomeLista = []

again = 's'

while again == 's':
    name = input('Aggiungi un nome: ')

    nomeLista.append(name)

    print('Desideri aggiungere un altro nome?')
    again = input('s = si, qualsiasi altra cosa = no: ')

print(nomeLista)

print('')




#metodo index - per restituire la posizione di un elemento nella lista

menu = ['hamburger', 'patatine', 'cocacola']

item = input('Quale prodotto devo modificare? ')

try:
    itemIndex = menu.index(item) #ottiene l'indice dell'elemento nella lista
    newItem = input('Inserisci un nuovo cibo: ')
    menu[itemIndex] = newItem #sostituisce il vecchio elemento con quello nuovo

    print('Ecco la lista modificata:')
    print(menu)
except ValueError:
    print('Non è possibile trovare questo elemento nella lista')

print('')





#metodo insert - consente di inserire uno specifico elemento in una posizione specifica della lista

coglioni = ['Culo', 'Cacca', 'Comunisti']

print(coglioni)

coglioni.insert(0,'Coglioniii')

print("Ecco la lista dopo l'insert")
print(coglioni)

print('')




#metodo sort - riordina la lista in ordine ascendente

numeriCacca = [0,1,5,6,3,9,8,4]
print('Sequenza originale', numeriCacca)

numeriCacca.sort()
print('Sequenza ordinata', numeriCacca)

print('')




#metodo remove - elimina il primo elemento corrispondente al valore passato come argomento
food = ['Pizza', 'Hamburger', 'Cazzi']

item = input('Quale valore vuoi sostituire? ')

try:
    food.remove(item)
    print('Ecco la lista modificata: ')
    print(food)

except ValueError:
    print('Impossibile trovare il valore nella lista')

print('')




#metodo reverse - inverte l'ordine degli elemente nella lista, senza creare una nuova lista
cazzoni = [5,4,3,2,1]
print(cazzoni)

cazzoni.reverse()
print('La lista dopo il metodo reverse: ', cazzoni)

print('')






#istruzione del - elimina l'elemento in una poszione specifica tramite l'indice != dal remove

sas = ['Culo', 'Cacca', 'Comunisti']
del sas[2]
print(sas)

print('')



#funzioni min e max - vabbe non lo spiego 
palle = [5,4,3,2,1]
print('Numero piu grande nella lista: ',max(palle))
print('Numero piu piccolo nella lista: ',min(palle))