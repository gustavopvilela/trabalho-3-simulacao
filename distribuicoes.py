import math

M = 2147483647
_seed = 1

def set_seed(s):
    global _seed
    if not 1 <= s <= M - 1:
        raise ValueError("Seed deve estar entre 1 e 2147483646")
    _seed = s

def uniforme () -> float:
    global _seed
    _seed = (16807 * _seed) % M
    return _seed / M

def beta (a, b):
    alfa = a + b
    if min(a, b) <= 1:
        bet = max(1 / a, 1/ b)
    else:
        bet = math.sqrt((alfa - 2) / (2 * a * b - alfa))
    gama = a + 1 / bet
    while True:
        u1 = uniforme()
        u2 = uniforme()
        v = bet * math.log(u1 / (1 - u1))
        w = a * math.exp(v)
        if alfa * math.log(alfa / (b + w)) + gama * v - 1.3862944 >= math.log(u1 * u1 * u2):
            return w / (b + w)

def pert (otimista, provavel, pessimista) -> float | None:
    if otimista == pessimista or not (otimista <= provavel <= pessimista):
        return None

    a = 1 + 4 * (provavel - otimista) / (pessimista - otimista)
    b = 1 + 4 * (pessimista - provavel) / (pessimista - otimista)
    return otimista + (pessimista - otimista) * beta(a, b)

def normal (media=0.0, desvio=1.0) -> float:
    u1 = uniforme()
    u2 = uniforme()
    z = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    return media + desvio * z

def lognormal (media_ln, desvio_ln):
    media = math.log((media_ln**2) / (math.sqrt(desvio_ln**2 + media_ln**2)))
    desvio = math.sqrt(math.log(1 + ((desvio_ln**2) / (media_ln**2))))

    return math.exp(normal(media, desvio))

def bernoulli (sucesso) -> int:
    return 1 if uniforme() < sucesso else 0

