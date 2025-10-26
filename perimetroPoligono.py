import math 

def distanza(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))


def main():
    perim = 0
    punti = 0
    while punti <= 2:
        punti = int(input("Da quanti punti è composto il poligono: "))
        print("Inserire le coordinate dei punti: ")
        xp = float(input("Inserire x primo punto "))
        yp = float(input("Inserire y primo punto "))
        x0 = xp
        y0 = yp
        for i in range(2,punti+1):
            xs = float(input("Inserire coordinata X del "+str(i)+" punto "))
            ys = float(input("Inserire coordinata X del "+str(i)+" punto "))
            perim += distanza(xp,yp,xs,ys)
            xp = xs
            yp = ys
            perim += distanza(xp,yp,x0,y0)
        print("Il perimetro è uguale a ", perim)

main()
