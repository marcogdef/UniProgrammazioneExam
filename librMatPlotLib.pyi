#IMPORTAZIONE LIBRERIA MATPLOTLIB E MODULO PYPLOT
import matplotlib.pyplot as plt

#FUNZIONE PLOT, PIANO CARTESIANO
def pianoCartesiano():
    xCoords = [0,1,2,3,4]
    yCoords = [0,5,2,6,4]

    plt.plot(xCoords, yCoords) #assegna le coordinate al grafico
    plt.title('Dati campione') #assegna il titolo
    
    plt.xlabel("Questo è l'asse x") #etichetta asse x
    plt.ylabel("Questo è l'asse y") #etichetta asse y

    plt.xlim(xmin=-1, xmax=10)#con xlim personalizziamo la grandezza del grafico su cui verranno 
    plt.ylim(ymin=-1, ymax=10) #mostrate le nostre coordinate

    plt.xticks(
        [0,1,2,3,4,5,6,7,8,9,10],
        ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'], #personalizza le tacche
    )
    plt.yticks(
        [0,1,2,3,4,5,6,7,8,9,10],
        ['0m', '1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m']
    )

    plt.plot(xCoords, yCoords, marker='o') #disegna un pallino sui punti
    
    plt.grid(True) #assegna al grafico una griglia in backgound
    plt.show() #lo stampa a video


def grafBarre():
    left_edges = [0,10,20,30,40]
    heights = [100,200,300,400,500]

    plt.bar(left_edges, heights, color='g', width=3) #assegna i valori al grafico, peronalizza il colore e lo spessore delle barre
    plt.show() #stampa il grafico


def grafTorta():
    values = [20,50,60,70]

    slice_labels = [
        '1 trim','2 trim','3 trim','4 trim' #associa a ogni fetta del grafico a torta un etichetta
    ]

    plt.pie(values, labels=slice_labels, colors=('r','g','m','k')) #assegna al grafico i valori e successivamente associa le etichette e colori a questi valori
    plt.title('Vendite')
    plt.show()
    

pianoCartesiano()
grafBarre()
grafTorta()


