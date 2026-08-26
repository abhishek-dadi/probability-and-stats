
def birth(n):
    prob = 1.0
    for i in range(n):
        prob *= (365 - i) / 365
    return 1 - prob


def generateprob():
    x = list(range(100))
    res = [birth(i) for i in x]
    return x, res