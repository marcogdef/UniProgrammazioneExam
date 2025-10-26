#a = int(input("inserisci a "))
#b = int(input("inserisci b "))

#while a <b:
    #print("il valore di a è " ,a)
    #a = a + 1
#print("fine del ciclo")    

    
     
#for num in ["GAY",2,3,4,5]:
    #print(num)
  
#for num in range(9):
    #print(num)

#for num in range(1,10,2):
    #print(num)

#acc = 0
#keep_going = input("Vuoi aggiungere un numero? Scrivi si per continuare ")
#while keep_going == "si":
    #num = int(input("aggiungi il numero "))
    #acc = acc + num
    #print(acc)
    #keep_going = input("vuoi aggiungere altri numeri?si o no ")
#print(acc)

#for hours in range(24):
    #for minutes in range(60):
        #for seconds in range(60):
            #print(hours, ";",minutes, ":", seconds)

#RIMBALZI DI UNA PALLINA
#altprima = float(input("Altezza primo rimbalzo in cm "))
#contatore = 0
#while altprima>1:
    #print("L'altezza ora è ", f"{altprima:.2f}")
    #print("numero di rimbalzi è", f"{contatore:.2f}")
    #altprima*=0.8
    #contatore = contatore + 1

#print("L'altezza finale della pallina è", altprima)    



#MEDIA DEI VOTI
#accumultore = 0
#somma = 0
#voto = int(input("Inserisci voto "))
#if voto>=0 and voto<=30:
    #while voto>=0 and voto<=30:
        #somma = somma + voto
        #accumultore = accumultore + 1
        #voto = int(input("Inserire voto "))
    #print("La somma è pari a", somma)
    #print("La media è pari a", float(somma)/accumultore)
#else:
    #print("Il voto non è valido")


#INPUT DI UN NUMERO CALCOLO QUANTE VOLTE +2 PER ARRIVARE A CENTO
#N = 100
#while N>98:
    #N = int(input("Inserisci il numero "))
#i = 0
#passo = int(input("Decidi il passo "))

#while N<100:
    #N+=passo
    #i+=1

#print("Per arrivare a 100 sono necessarie", i, "somme con ", passo)    

#GESTIONE SOMMA NUMERI POSITIVI O NEGATIVI
#num = "0"
#sommanp = 0
#sommann = 0
#while num != 0:
    #num = int(input("Inserisci numero o scrivi 0 per concludere: "))
    #if num>0:
        #sommanp+=num
    #else:
        #sommann+=num
#print("La somma dei numeri positivi è", sommanp)
#print("La somma dei numeri negativi è", sommann)


#LIBRERIE
#MODULO RANDOM
#import random

#number = random.randrange(0,40) #o random.randit ecc
#print(number)

#MODULO LOCALE
#import locale

#locale.setlocale(locale.LC_ALL, 'it_IT')

#number = locale.atof(input("Inserisci numero "))
#print(number)