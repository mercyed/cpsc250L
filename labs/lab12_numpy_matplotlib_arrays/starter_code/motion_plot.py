import numpy as np
import matplotlib.pyplot as plt

def position(t, x0, v0, a):
    return  x0 + v0 * t + 0.5 * a * t**2


def velocity(t, v0, a):
    return v0 + a * t

def main():
    # Consider a projectile launched at a speed of 50 m/s and an angle of 45 degrees.
    #
    # Goal: create plots of x vs. t, y vs. t, v_x vs. t, and v_y vs. t
    #       for 0 < t < 10 seconds
    #
    # TODO: create time array using np.linspace
    # TODO: compute position and velocity arrays
    # TODO: make and save plots
    pass


main()
