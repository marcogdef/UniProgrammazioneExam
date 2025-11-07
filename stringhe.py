#STRINGHE (sono immutabili)

#accesso ai caratteri di una stringa tramite ciclo for
palle = 'ciaooo'
for i in palle:
    print(i)

print('')


#verifica caratteri speciali
count = 0
my_string = input('Inserisci una frase: ')
for i in my_string:
    if i == 'T' or i == 't':
        count += 1
print(f'La lettera T compare {count} volte.')

print('')


#accesso per indicizzazione
stringa = 'palle piedi e cardoncelli'
ch = stringa[9]
chminus = stringa [-1]
print(ch)
print(chminus)

print('')


#funzione len sulle stringhe
city = 'Boston'
index = 0

while index< len(city):
    print(city[index])
    index+=1

print('')


#concatenazione di stringhe
message = 'ciao ' + 'mondo'
print(message)

letters = 'abc'
letters += 'def' #la stringa abc non viene modificata ma viene creata una nuova stringa assegnata a letters

print('')


#slicing nelle strighe
fullname = 'Marco Giovanni Defronzo'
firstname = fullname[:14]
print(firstname)
print(fullname[15:]) #si possono inserire anche i valori di incremento

fullname2 = fullname[:] #cosi ho copiato la stringa in un altra variabile
print(fullname2)

