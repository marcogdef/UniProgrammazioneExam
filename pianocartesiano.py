def main():
    primoX = float(input("Inserisci il primo punto X: "))
    primoY = float(input("Inserisci il primo punto Y: "))
    secondoX = float(input("Inserisci il secondo punto X: "))
    secondoY = float(input("Inserisci il secondo punto Y: "))
    distanza = calcoloD(primoX,primoY,secondoX,secondoY)
    print("La distanza è di: ", distanza)




def calcoloD(x1,y1,x2,y2):
    distanza = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return distanza


    
main()