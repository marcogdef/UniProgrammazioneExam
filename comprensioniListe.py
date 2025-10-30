#COMPRENSIONE DI LISTA
#molto piu veloci

list = [1,2,3,4,5]
list2 = [item for item in list] #duplicare una lista
print(list2)    #un semplice ciclo for solo che ad ogni iterazione del for 
                #l'elemento corrente passato nel for viene inserito nella variabile 'item'

#\\\\\\\\\\\

list3 = [1,2,3,4,5]
list4 = [item**2 for item in list3] #elevazione a potenza
print(list4)


#calcolo lunghezza stringhe

strlist = ['cazzi', 'palle', 'pippii']
lenlist = [len(s) for s in strlist]
print(lenlist)



#filtraggio con IF nei cicli

list5 = [2,5,9,12,56,233]
list6 = []

for n in list5:
    if n < 10: #IF permette di assegnare alla lista list6 i valori minori di 10 contenuti in list5
        list6.append(n)

print(list6)



#comprensione di lista con if con numeri

list7 = [2,5,9,12,56,233]
list8 = [n for n in list7 if n<10] #'n' iniziale è come un risultato di tutto il ciclo successivo 
                                   #cio che verrà poi inserito nella list8 
print(list8)



#comprensione di lista con if con stringhe

list9 = ['antonello', 'marco', 'vittoria', 'elena']
list10 = [name for name in list9 if len(name)<6] #aggiunge alla list10 solo i nomi con meno di 6 lettere
print(list10)


