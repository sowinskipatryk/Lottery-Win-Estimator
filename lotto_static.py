import numpy as np
import matplotlib.pyplot as plt
import random


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


lucky = 6
balls = 49
moves = int((factorial(balls)/(factorial(balls-lucky)*factorial(lucky))))

listx = []
listy = []
means = []
arrx = np.array(listx)
arry = np.array(listy)
arrm = np.array(means)

for x in range(100):
    arrx = np.append(arrx, x+1)
    arry = np.append(arry, shuffle(moves))
    arrm = np.append(arrm, np.mean(arry))

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.scatter(arrx, arry)
ax1.set_title('Tries')
ax1.axhline(y=moves, color='r', linestyle='--')
ax2.plot(arrx, arrm)
ax2.set_title('Deviation from the mean after n draws')
ax2.axhline(y=moves, color='r', linestyle='--')

ax1.set(xlabel='Draw Number', ylabel='Tries to succeed')
ax2.set(xlabel='Draw Number', ylabel='Mean')

plt.show()
