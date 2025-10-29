def main():

    #SCRIVO (WRITE)
    numRec = int(input('quanti record dei dipendenti ' + 'desideri creare? '))

    empFile = open('employees.txt', 'w')

    for count in range(1, numRec+1):
        print(f'Inserisci i dati del dipendente {count}')
        name = input('Nome: ')
        id = input('Codice: ')
        reparto = input('Reparto: ')

        empFile.write(f'{name}\n')
        empFile.write(f'{id}\n')
        empFile.write(f'{reparto}\n')

        print()

    empFile.close()
    print("Record scritti nel file employees.txt")
    
    #LEGGO (READ)
    empFile = open('employees.txt', 'r')
    name = empFile.readline()

    while name!= '':
        id = empFile.readline()
        reparto = empFile.readline()

        name = name.rstrip('\n')
        id = id.rstrip('\n')
        reparto = reparto.rstrip('\n')

        name = empFile.readline()   
        

    empFile.close()

main()

