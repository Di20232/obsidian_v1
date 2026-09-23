import math
print(math.sqrt(16))
print(math.pi)

from math import sqrt, pi
print(sqrt(25))
print(pi)

import random
import datetime
import os

print(random.randint(1, 10))
print(datetime.date.today())
print(os.getcwd())

# Exercício resolvido: simular lançamento de dado 5 vezes
for _ in range(5):
    print(random.randint(1, 6))
