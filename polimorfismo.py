#POLIMORFISMO E OVERRIDING (Il termine polimorfismo indica la capacità di un oggetto di prendere forme diverse.)
#(L’overriding è la definizione di un metodo in una sottoclasse con lo stesso nome del metodo nella superclasse.)

class Mammal:
    def __init__(self, species):
        self.__species = species
    
    def show_species(self): #metodo get 
        print('Io sono un', self.__species)
    
    def make_sound(self): 
        print('Grrrr')


class Dog(Mammal): #sottoclasse di Mammal
    def __init__(self):
        Mammal.__init__(self,'Cane') #nel metodo init ricreiamo il metodo init della superclasse (passandoli 'cane'), ma ridefinendolo per eseguire azioni piu appropriate per un cane
    
    def make_sound(self): #overriding del metodo make_sound che fa riferimento al cane
        print('Bau! Bau!') 


class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Gatto')
    
    def make_sound(self):
        print('Miao!') 


