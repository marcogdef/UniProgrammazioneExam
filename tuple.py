#LE TUPLE
#Sono delle liste che non sono modificabili e rimangono invariate

myTuple = (1,2,3,4,5)
print(myTuple)

print('')




#iterazione for sulle tuple
names = ('giacomo', 'paolo', 'paola', 'piedina')

for n in range(len(names)): #len(names) fa si che il valore passato ad n sia solo un nome (quindi piu preciso)
    print(names[n]) 

print('')



#conversione fra liste e tuple
number_tuple = (1,2,3,4)
number_list = list(number_tuple)
print(number_list)
number_list.append(8) #ora la tuple è una lista quindi modificabile
print(number_list)


str_list = ['piedini', 'pallette', 'ommagad']
str_tuple = tuple(str_list)
print(str_tuple) #abbiamo trasformato una lista in una tuple