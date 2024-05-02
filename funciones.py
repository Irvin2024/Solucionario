def es_primo(numero):
    i=2
    while i<=numero//2:
        if numero%i==0:
            return False
        i+=1
    return True

def factorial(numero):
    i=1
    fact=1
    while i<numero:
        i+=1
        fact=fact*i
    return fact
def serie_primos(n):
    i=1
    v=2
    while i<=n:
        if es_primo(v):
            print(v,end=" ")
            i+=1
        v = v + 1

def serie_primos_naturales(n):
    i=1
    v=2
    while i<=n:
        if es_primo(v):
            print(str(i)+"/"+str(v),end=" ")
            i+=1
        v = v + 1

def serie_fracciones(n):
    i=1
    while i<=n:
        print(str(i)+"/"+str(i+1),end=" ")
        i+=1
def primo_n(numero):
    i=2
    primo=1
    valor=0
    while primo<=numero:
        if es_primo(i):
            primo+=1
            valor=i
        i+=1
    return valor