import time
def zmierz(f, n=100):
    """Funkcja mierzy czas działania funkcji f dla danego argumentu n"""
    t0=time.time()
    
    f(n)
    t1=time.time()
    return t1 - t0
def silnia_rek(n):
    """Funkcja liczy silnię n rekurencyjnie"""
    if n > 1:
        return silnia_rek(n-1)*n
    else:
        return 1
def silnia_it(n):
    """Funkcja liczy silnię n iteracyjnie"""
    a = 1
    for i in range(1,n+1):
       a = a * i
    return a
print("Silnia rekurencyjnie: ",zmierz(silnia_rek),"s, Silnia iteracyjnie: ",zmierz(silnia_it),"s")