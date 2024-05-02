def es_primo(numero):
    i=2
    while i<=numero//2:
        if numero%i==0:
            return False
        i+=1
    return True
def primo_n(numero):
    i=2
    primo=1
    valor=0
    while primo<=numero:
        if es_primo(i):
            primo+=1
            valor=i
        i+=1
    print("El n-simo primo es: ",valor)

primo_n(6)