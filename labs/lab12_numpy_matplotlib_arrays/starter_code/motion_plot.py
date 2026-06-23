import numpy as np
import matplotlib.pyplot as plt

def position(t, x0, v0, a):
    return x0 + v0 * t + 0.5 * a * t**2


def velocity(t, v0, a):
    return v0 + a * t

def main():
    # Consider a projectile launched at a speed of 50 m/s and an angle of 45 degrees.
    #
    # Goal: create plots of x vs. t, y vs. t, v_x vs. t, and v_y vs. t
    #       for 0 < t < 10 seconds
    #
    # TODO: create time array using np.linespace
    # TODO: compute position and velocity arrays
    # TODO: make and save plots
    speed = 50
    angle = np.radians(45)

    vx0 = speed * np.cos(angle)
    vy0 = speed * np.sin(angle)

    ax = 0
    ay = -9.8

    t = np.linspace(0, 10, 100)

    x = position(t, 0, vx0, ax)
    y = position(t, 0, vy0, ay)

    vx = velocity(t, vx0, ax)
    vy = velocity(t, vy0, ay)

    plt.figure()
    plt.plot(t, x)
    plt.xlabel("Time (s)")
    plt.ylabel("x position (m)")
    plt.title("x vs. t")
    plt.savefig("x_vs_t.png")

    plt.figure()
    plt.plot(t, y)
    plt.xlabel("Time (s)")
    plt.ylabel("y position (m)")
    plt.title("y vs. t")
    plt.savefig("y_vs_t.png")

    plt.figure()
    plt.plot(t, vx)
    plt.xlabel("Time (s)")
    plt.ylabel("x velocity (m/s)")
    plt.title("vx vs. t")
    plt.savefig("vx_vs_t.png")

    plt.figure()
    plt.plot(t, vy)
    plt.xlabel("Time (s)")
    plt.ylabel("y velocity (m/s)")
    plt.title("vy vs. t")
    plt.savefig("vy_vs_t.png")

    plt.show()



main()
