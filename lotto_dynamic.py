import matplotlib.pyplot as plt
import numpy as np
import random

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


moves = int((factorial(ALL_BALLS) / (factorial(ALL_BALLS - LUCKY_BALLS) *
                                     factorial(LUCKY_BALLS))))

list_x = []
list_y = []
list_means = []

plt.ion()

min_x = 0
max_x = 100

fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ln1, = ax1.plot([], [], 'o')
ln2, = ax2.plot([], [])

ax1.set_autoscaley_on(True)
ax1.set_xlim(min_x, max_x)
ax1.set_title('Tries')
ax1.axhline(y=moves, color='r', linestyle='--')
ax1.set(xlabel='Draw Number', ylabel='Tries to succeed')

ax2.set_autoscaley_on(True)
ax2.set_xlim(min_x, max_x)
ax2.set_title('Mean deviation')
ax2.axhline(y=moves, color='r', linestyle='--')
ax2.set(xlabel='Draw Number', ylabel='Mean')

for x in np.arange(max_x):
    list_x.append(x)
    list_y.append(shuffle(moves))
    list_means.append(np.mean(list_y))

    ln1.set_xdata(list_x)
    ln1.set_ydata(list_y)
    ln2.set_xdata(list_x)
    ln2.set_ydata(list_means)

    ax1.relim()
    ax1.autoscale_view()
    ax2.relim()
    ax2.autoscale_view()

    fig.canvas.draw()
    fig.canvas.flush_events()
