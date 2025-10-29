#LE LISTE2

lista1 = [1,2,3,4,5]
lista2 = lista1

print(lista1)
print(lista2)

lista1[0] = 99

print(lista1)
print(lista2) #list1 e list2 sono la stessa cosa, infatti dopo aver modificato 
              #l'indice 0 entrambe risulteranno con 99


#copia di liste

lista3 = [1,2,3,4]
lista4 = [] #creazione lista vuota

for item in lista3:
    lista4.append(item) #metodo append copia il contenuto di lista3 in quello di lista4 rendendole identiche ma separate
print(lista4)


#altro metodo per duplicare una lista

lista5 = [1,2,3,4,5]
lista6 = [] + lista5
print(lista6)