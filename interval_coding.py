from elias_coding import elias_intervals
from arithmetic_coding import arithmetic_intervals
from collections import Counter


chars = []
with open('pagina.txt') as pag:
    for line in pag:
        for char in line:
            if char != ' ':
                chars.append(char)

frecuencies = Counter(chars).most_common()


# Codifica por intervalos en base a
def interval_coding(mensaje, intervalos):
    """
    Limites inferior y superior
    Inferior = AI + (AS - AI) * NI
    Superior = AI + (AS - AI) * NS
    AI = Antiguo Inferior   AS = Antiguo Superior
    NI = Nuevo Inferior     NS = Nuevo Superior
    """

    compression_ratio = ''
    antiguo = (0.0, 1.0)
    nuevo = intervalos.get(mensaje[0])

    for i in xrange(1, len(mensaje)):
        inferior = antiguo[0] + ((antiguo[1] - antiguo[0]) * nuevo[0])
        superior = antiguo[0] + ((antiguo[1] - antiguo[0]) * nuevo[1])
        nuevo = intervalos.get(mensaje[i])
        antiguo = (inferior, superior)
    inferior = antiguo[0] + ((antiguo[1] - antiguo[0]) * nuevo[0])
    superior = antiguo[0] + ((antiguo[1] - antiguo[0]) * nuevo[1])

    compression_ratio = superior / sum([frecuency[1] for frecuency in frecuencies if frecuency[0] in mensaje])
    # compression_ratio = steps * 100 / len(mensaje)
    return inferior, superior, compression_ratio


