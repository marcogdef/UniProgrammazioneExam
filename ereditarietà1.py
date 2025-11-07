#EREDITARIETA

class Automobile: #superclasse 
    def __init__(self, marca, model, km, price):
        self.__marca = marca
        self.__model = model
        self.__km = km
        self.__price = price

    def set_marca(self, marca):
        self.__marca = marca

    def set_model(self, model):
        self.__model = model

    def set_km(self, km):
        self.__km = km

    def set_price(self, price):
        self.__price = price

    def get_marca(self):
        return self.__marca

    def get_model(self):
        return self.__model

    def get_km(self):
        return self.__km

    def get_price(self):
        return self.__price

        

class Car(Automobile): #sottoclasse di Automobile
    def __init__(self, marca, model, km, price, doors): #car eredita tutti gli attributi di Automobile e aggiunge doors
        super().__init__(marca, model, km, price) #super.init richiama la funzione init della superclasse passandoli gli attributi
        self.__doors = doors #inizializza anche l'atttributo privato aggiunto
    
    def set_doors(self, doors):
        self.__doors = doors
    
    def get_doors(self):
        return self.__doors
    

class Truck(Automobile): #sottoclasse di Automobile
    def __init__(self, marca, model, km, price, drive_type):
        super().__init__(marca, model, km, price)
        self.__drive_type = drive_type
    
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
    
    def get_drive_type(self):
        return self.__drive_type
    

class SUV(Automobile): #sottoclasse di Automobile
    def __init__(self, marca, model, km, price, pass_cap):
        super().__init__(marca, model, km, price)
        self.__pass_cap = pass_cap
    
    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap