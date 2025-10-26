def primo(n):
    
    div = 2
    while div<n:
        if n%div==0:
            return False #FALSE SOLO SE IL NUMERO NON è PRIMO, APPENA LA DIVISIONE SARA' CON RESTO 0
                         #LA FUNZIONE SI STOPPERà A RETURN FALSE SENZA ESEGUIRE ALTRI PROCEDIMENTI E NON SI STAMPERA' LA i del for
        div+=1
    return True

        

def main():
    num = 0
    while num<=3:
        num = int(input("Inserire numero "))

    print("1,2", end=", ")
    for i in range (3,num+1,2):
        if primo(i):
            print(i,end=", ")
    

main()