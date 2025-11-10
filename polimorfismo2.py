import polimorfismo

mammal = polimorfismo.Mammal('Mammifero standard') #creiamo un oggetto 
mammal.show_species()
mammal.make_sound()

dog = polimorfismo.Dog() #creiamo l'oggetto della classe dog
dog.show_species() #Io sono un 'cane'(Non ce bisogno di una ridefinizione di show_species nella classe dog perche passiamo a Mammal 'Cane' (species))
dog.make_sound() #'Bau!, Bau!'

cat = polimorfismo.Cat() #creiamo l'oggetto della classe cat
cat.show_species()
cat.make_sound() 



#funzione polimorfistica (senza nessun errore alle sue chiamate)
#def show_mammal_info(creature): #questa funzione non fa riferimento ne a mammal ne a dog ne a cat, infatti puo puntare a tutti e 3
    #creature.show_species()
    #creature.make_sound()

#funzione polimorfistica 
def show_mammal_info(creature):
    if isinstance(creature, polimorfismo.Mammal): #controllo isinstance è uguale a 'è creature(quindi quello che viene passato alla funzione) un istanza o una sottoclasse di Mammal?'
        creature.show_species()
        creature.make_sound()
    else:
        print('Questo non è un mammifero')
    
    
show_mammal_info(mammal) #passeremo noi alla funzione quando la chiamaremo la classe a cui dovrà ar riferimento
print('')
show_mammal_info(dog)
print('')
show_mammal_info(cat)
print('')
show_mammal_info('I a string') #qui ce l'errore perche la stringa non fa riferimento a nessuna classe


