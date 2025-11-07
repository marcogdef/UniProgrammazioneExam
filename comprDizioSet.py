#COMPRENSIONE DI DIZIONARIO -- legge sequenza di elementi in input e li inserisce in un dizionario 
numbers = [1,2,3,4,5]
 
squares = {}

squares = {item: item**2 for item in numbers} #item:item**2 è il risultato del for quindi con questa comprensione verranno create delle chiave:valore con elemento:elemento**2
print(squares)


#USO DI DIZIONARI COME INPUT
phonebook = {'Chris': '555-1111', 'Katie': '555-2222','Joanne': '555-3333'}

phonebook_copy = {k: v for (k, v) in phonebook.items()} #il risultato è una copia di phonebook con una comprensione in cui k:v sono la chiave:valore
#per ogni k:v in phonebook si assegnano gli elementi a k:v di phonebook_copy


#COMPRENSIONI CON IF
populations = {
'New York': 8398748,
'Los Angeles': 3990456,
'Chicago': 2705994,
'Houston': 2325502,
'Phoenix': 1660272,
'Philadelphia': 1584138
}

largest = {}

#for k, v in populations.items(): #si scorre ogni elemento chiave:valore del dizionario
    #if v > 2000000: #per ogni elemento ce la condizione if per capire se la popolaizone è maggiore a 2000000 
        #largest[k] = v #se population(v) è maggiore di 2000000 la coppia chiave:valore viene inserita nel dizionario largest
#print(largest)

largest = {k: v for k, v in populations.items() if v > 2000000} #comprensione del for di sopra --- k:v all'inzio è la chiave:valore che verra inserita in largest se la condizone if verrà eseguita
print(largest) 






#COMPRENSIONE DI SET -- legge sequenza di elementi in input e li inserisce in un set
set1 = set([1,2,3,4,5])
set2 = {item for item in set1} #comprensione del for per assegnare i valori di set1 a se2
print(set2)


#COMPRENSIONE CON IF 
set3 = set([1,20,30,2,4,70])
set4 = {item for item in set3 if item<10} #comprensione con if cicla tutti gli elementi di set3 e aggiunge a set 4 solo gli elementi di set3<10
print(set4)