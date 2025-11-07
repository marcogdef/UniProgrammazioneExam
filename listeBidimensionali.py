#LISTE BIDIMENSIONALI
#Liste composte da righe e colonne

values = [
    [1,2,3],
    [10,20,30],
    [100,200,300]
]

for row in values:
    for element in row:
        print(element) #stampa i dati della lista 

print('')





#modifica di liste bidimensionali

import random
rows = 3
cols = 4

def main():
    valori = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    for r in range(rows):
        for c in range(cols):
            valori[r][c] = random.randint(1,100)
    
    print(valori)

main()