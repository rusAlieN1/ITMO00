def add_fractions(a, b, c, d):
    y = c * d
    if y <= 0: return "ОШИБКО"
    x = a * d + b * c
    for i in range(1, max(x, y)):
        if x % i == 0 and y % i == 0:
            NOK = i
    return (x/NOK, y/NOK)
print (add_fractions(4, 24, 4, 48))
