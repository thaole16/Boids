"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes

boid_count = 50
x_positions = [-450, 50.0]
y_positions = [300.0, 600.0]
x_velocities = [0, 10.0]
y_velocities = [-20.0, 20.0]

boids_x = np.random.uniform(size=boid_count,*x_positions)
boids_y = np.random.uniform(size=boid_count,*y_positions)
boid_x_velocities = np.random.uniform(size=boid_count, *x_velocities)
boid_y_velocities = np.random.uniform(size=boid_count, *y_velocities)
boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)


def update_boids(boids):
    xs, ys, xvs, yvs = boids
    move_to_middle_strength = 0.01
    # Fly towards the middle
    for i in range(len(xs)):
        xvs[i] = xvs[i] + (np.mean(xs) - xs[i]) * move_to_middle_strength
        yvs[i] = yvs[i] + (np.mean(ys) - ys[i]) * move_to_middle_strength
    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 100:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] + (ys[i] - ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 10000:
                xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * 0.125 / len(xs)
                yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * 0.125 / len(xs)
    # Move according to velocities
    for i in range(len(xs)):
        xs[i] = xs[i] + xvs[i]
        ys[i] = ys[i] + yvs[i]


figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
