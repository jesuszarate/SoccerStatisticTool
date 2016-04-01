
pierde = -2
empata = 0.2
gana = 1

#Assume a tuple (p, e, g)
def compute(t):
    return (pierde * t[0]) + (empata * t[1]) + (gana * t[2])
