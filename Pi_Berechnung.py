# Pi Berechnung nach Leibniz

import time
pi = 0.0
n = int(input("Bitte eine ganze Zahl zwischen 1 und 10000000 eingeben:"))

if n <= 10000000:
    for i in range(0, n+1, 1):
        summe = 4*((-1)**i/(2*i+1))
        pi += summe
    print('\n' "Pi beträgt nach {} Iterationen den folgenden Wert: {}".format(i, pi) '\n')

else:
    print('\n' "Diese Zahl ist aushalb des Bereiches!" '\n')