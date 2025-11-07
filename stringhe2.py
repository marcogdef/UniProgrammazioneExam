#operatore IN nelle stringhe

text = 'Quarantaquattro gatti in fila per sei col resto di due'

if 'sei' in text: #si puo usare anche not in
    print('La riga è stata trovata')
else:
    print('La stringa non è stata trovata')

print('')



#METODI DI STRINGHE

#metodo isdigit ritorna true se la stringa contiene solo numeri
string1 = '1234'

if string1.isdigit():
    print(f'{string1} contiene solo numeri')
else:
    print(f'{string1} non contiene solo numeri')

#combinazione di metodi
user_string = input('Inserisci una stringa: ')

if user_string.isalnum():
    print('La stringa è alfanumerica')
if user_string.isdigit():
    print('La stringa contiene solo numeri')
if user_string.isalpha():
    print('La stringa contiene solo lettere')
if user_string.isspace():
    print('La stringa contiene solo spazi bianchi')
if user_string.islower():
    print('La stringa contiene solo minuscole')
if user_string.isupper():
    print('La stringa contiene solo maiuscole')

print('')


#METODI PER LA MODIFICA DI STRINGHE (sono immutabili creano una copia)
#lower, istrip, istrip(char), rstrip, strip(char), upper

#lower trasforma tutti i caratteri in minuscolo
letters = 'YTZgh'
print(letters.lower())

#upper traforma tutti i caratteri in maiuscolo
lettere = 'ciaoPorcodio'
print(lettere.upper())

#metodo upper in un ciclo
again = 's' 

while again.upper() == 's': #s o S inserito dall'utente non cambia perche se fosse S maiuscolo il metodo lo converte a minuscolo quindi l'utente non potra sbagliare
    print('Vuoi vedere di nuovo questo messaggio?')
    again = input('s = si, qualsiasi altra cosa no')

print('')



#SOTTOSTRINGHE METODI PER LA RICERCA E MODIFICA
#endswith, find, replace, startswith

string = 'Quarantaquattro gatti in fila per sei col resto di due'
position = string.find('sei') #individua l'indice

if position != -1: #-1 perche il metodo find restituisce -1 se la sottostringa non viene trovata
    print(f'La parola "sei" è stata trovata alla posizione {position}') 
else:
    print('La parola "sei" non è stata trovata.')


#metodo replace
newstring = string.replace('gatti', 'ragni') #replace rimpiazza la sottostringa gatti con ragni
print(newstring)


#metodo split
lista = 'uno due tre quattro'
wordlist = lista.split() #divide le quattro parole in una lista 
print(wordlist)



