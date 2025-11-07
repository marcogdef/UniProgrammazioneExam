#SET sono mutabii (non possono contenere valori uguali)

myset = set(['a','b','c']) #set di stringhe in una lista
set1 = set('abc') #passiamo come argomento una stringa --- avrà lo stesso numero di elementi di un set di stringhe (a,b,c)
#my_set = set('aaabc') #set non possono contenere valori uguali quindi verranno eliminate i due elementi 'a'


#OPERAZIONI SUI SET
#LEN
print(len(myset)) #LEN per sapere la lunghezza di un set

#ADD
set2 = set()

set2.add(1) #ADD aggiune il valore 1
set2.add(2)
set2.add(3)

set2.add(2) #non solleva un eccezione ma semplicemente non aggiunge nessun elemento

print(set2)


#UPDATE
set2.update([4,5,6]) #UPDATE aggiorna il set con i nuovi valori assegnati
print(set2)
#/////////////
myset.update(set2) #aggiorna myset aggiungendo i valori di set2 quindi un set che comprende sia numeri sia stringhe
print(myset)
print(set2) #set2 invece rimane invariato


#REMOVE e DISCARD
myset.remove(1) #rimuove il valore 1 dal set
myset.discard(5) #discard fa la stessa cosa ma a differenza di remove non solleva eccezioni 
print(myset)


#ITERARE I SET CON IL CICLO FOR CON IN 
for val in myset:
    print(val) #cicliamo tutti gli elementi di myset e successivamente li stampiamo


#TESTARE UN VALORE CON IF CON OPERATORE IN
if 3 in myset:
    print('Il valore 3 si trova in myset')

if 99 not in myset:
    print('Il valore 99 non si trova in myset')



#OPERAZIONI INSIEMISTICHE SUI SET
#METODO UNION
set3 = set([1,2,3,4])
set4 = set([5,6,7,8,])

set5 = set3.union(set4) #union permette di unire i due set(3,4) e successivamente assegnare questa unione alla variabile set5
print(set5)


#INTERSECTION O E COMMERCIALE
set3.update([6,7]) #aggiorno set3 cosi da provare intersection
set6 = set3.intersection(set4) #intersection permette di trovare i valori uguali presenti sia in set3 che in set4 e assegnarli alla variabile set6
print(set6)


#DIFFERNCE or -
set7 = set3.difference(set4) #difference permette di trovare i valori che si trovano solo in set3 (quindi non compresi anche in set4) e assegnarli alla variabile set7
print(set7)


#SYMMETRIC_DIFFERENCE
set4.update([3,4]) #aggiorno per fare la prova
set8 = set3.symmetric_difference(set4) #symmetric_difference trova i valori che non sono presenti in entrambi i set 
print(set8)


#ISUBSET E ISUPERSET (quando i due set contengono gli stessi valori)
set10 = set([1,2,3,4])
set11 = set([2,3])

set11.issubset(set10) #set11 è subset(sottoinsieme) di set10
set10.issuperset(set11) #set10 è superset(soprainsieme) di set11



