def main():

    variabile_file = open('piedini.txt', 'w')
    testo = input("Cosa vuoi inserire nel file: ")
    variabile_file.write(testo)
    variabile_file.close()

    condizione = int(input("Inserisci 1 per leggere il file "))
    if condizione == 1:
        variabile_file = open('piedini.txt', 'r')
        contenutifile = variabile_file.read()
        variabile_file.close()
        print(contenutifile)



main()


