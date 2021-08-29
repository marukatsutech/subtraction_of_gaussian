# Subtraction of 2 Gaussian functions
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update(f):
    ax.cla()  # Clear ax
    set_axis()

    global mu, direction
    ax.text(x_min, y_max * 0.9, " mu= +/-" + str(f'{mu:.1f}'))
    # Draw gaussian function
    y0 = 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(- (x - mu) ** 2 / (2 * sigma ** 2))
    y1 = - 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(- (x - (-mu)) ** 2 / (2 * sigma ** 2))
    ax.plot(x, y0, linestyle='--')
    ax.plot(x, y1, linestyle=':')
    ax.plot(x, y0 + y1)
    # Change mu
    mu += stp * direction
    if mu > x_max or mu < x_min:
        direction = - direction


def set_axis():
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title('Subtraction of 2 Gaussian functions')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()


# Global variables
x_min = -10.
x_max = 10.
y_min = -0.5
y_max = 0.5

mu = 0.
sigma = 1.
x = np.linspace(x_min, x_max, 100)

stp = 0.2
direction = 1.

# Generate figure and axes
fig = plt.figure()
ax = fig.add_subplot(111)

# Draw animation
set_axis()
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()
