import numpy as np
import matplotlib.pyplot as plt
import random

DRAWS = 100
LUCKY_BALLS = 6
ALL_BALLS = 49


def factorial(x):
    if x < 1:
        return 0
    elif x == 1:
        return 1
    else:
        return factorial(x-1) * x


def shuffle(n):
    i = 0
    while True:
        i += 1
        if not random.randrange(n):
            return i


moves = int((factorial(ALL_BALLS)/(factorial(ALL_BALLS-LUCKY_BALLS)*factorial(
    LUCKY_BALLS))))

list_x = []
list_y = []
list_means = []

for x in range(DRAWS):
    list_x.append(x)
    list_y.append(shuffle(moves))
    list_means.append(np.mean(list_y))

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.scatter(list_x, list_y)
ax1.set_title('Tries')
ax1.axhline(y=moves, color='r', linestyle='--')
ax1.set(xlabel='Draw Number', ylabel='Tries to succeed')

ax2.plot(list_x, list_means)
ax2.set_title('Deviation from the mean after n draws')
ax2.axhline(y=moves, color='r', linestyle='--')
ax2.set(xlabel='Draw Number', ylabel='Mean')

plt.show()
