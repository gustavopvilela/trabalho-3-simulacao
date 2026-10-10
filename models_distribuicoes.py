"""
Agrega os atributos das distribuições em classes para facilitar a visualização
"""

class PERT:
    o: float # Valor otimista (mínimo)
    m: float # O valor mais provável (moda)
    p: float # O valor pessimista (máximo)

    def __init__(self, o: float, m: float, p: float) -> None:
        self.o = o
        self.m = m
        self.p = p

class Normal:
    media: float # A média da distribuição.
    desvio: float # O desvio padrão da distribuição

    def __init__(self, media: float, desvio: float) -> None:
        self.media = media
        self.desvio = desvio

class LogNormal:
    media_ln: float # A média do logaritmo natural da variável.
    desvio_ln: float # O desvio padrão do logaritmo natural da variável

    def __init__(self, media_ln: float, desvio_ln: float) -> None:
        self.media_ln = media_ln
        self.desvio_ln = desvio_ln

class Bernoulli:
    p: float # A probabilidade de sucesso (ocorrência do evento = 1)

    def __init__(self, p: float) -> None:
        self.p = p