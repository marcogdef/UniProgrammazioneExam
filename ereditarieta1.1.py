import ereditarietà1

def main():
    used_car = ereditarietà1.Car('Audi', 2007, 12500, 21500.00, 4) #crea un oggetto della classe car chiamato used_car
    used_truck = ereditarietà1.Truck('BMW', 2009, 15000, 9000.00,'4wd')
    used_suv = ereditarietà1.SUV('Volvo', 2000, 30000, 18500.0, 5)
    
    print('MAGAZZINO AUTO USATE')
    print('====================')

    print('In magazzino è presente questa auto')
    print('Marca:', used_car.get_marca())
    print('Modello:', used_car.get_model())
    print('Chilometraggio:', used_car.get_km())
    print('Prezzo:', used_car.get_price())
    print('Numero di porte:', used_car.get_doors())
    print('')

    print('In magazzino è presente questo truck')
    print('Marca:', used_truck.get_marca())
    print('Modello:', used_truck.get_model())
    print('Chilometraggio:', used_truck.get_km())
    print('Prezzo:', used_truck.get_price())
    print('Numero di porte:', used_truck.get_drive_type())
    print('')

    print('In magazzino è presente questo SUV')
    print('Marca:', used_suv.get_marca())
    print('Modello:', used_suv.get_model())
    print('Chilometraggio:', used_suv.get_km())
    print('Prezzo:', used_suv.get_price())
    print('Numero di porte:', used_suv.get_pass_cap())

if __name__ == '__main__':
    main() 
