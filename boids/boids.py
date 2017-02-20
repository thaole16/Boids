"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random

# Deliberately terrible code for teaching purposes



class Boids(object):

    def __init__(self,
                 boid_count = 50,
                 x_positions = [-450, 50.0],
                 y_positions = [300.0, 600.0],
                 x_velocities = [0, 10.0],
                 y_velocities = [-20.0, 20.0] ):
        self.boids_x = np.random.uniform(size=boid_count,*x_positions)
        self.boids_y = np.random.uniform(size=boid_count,*y_positions)
        self.boid_x_velocities = np.random.uniform(size=boid_count, *x_velocities)
        self.boid_y_velocities = np.random.uniform(size=boid_count, *y_velocities)
        self.boids = (self.boids_x, self.boids_y, self.boid_x_velocities, self.boid_y_velocities)

    def update_boids(self, boids):
        xs, ys, xvs, yvs = boids
        move_to_middle_strength = 0.01
        alert_distance = 100
        formation_flying_distance = 10000
        formation_flying_strength = 0.125
        # Fly towards the middle
        x_move_to_middle = (np.mean(xs) - xs) * move_to_middle_strength
        y_move_to_middle = (np.mean(ys) - ys) * move_to_middle_strength
        xvs[:] = np.add(xvs, x_move_to_middle)
        yvs[:] = np.add(yvs, y_move_to_middle)

        x_separation = xs[np.newaxis, :] - xs[:, np.newaxis]
        y_separation = ys[np.newaxis, :] - ys[:, np.newaxis]
        separation_distance_squared = x_separation ** 2 + y_separation ** 2

        # Fly away from nearby boids
        birds_outside_alert = separation_distance_squared > alert_distance
        close_x_separations = np.copy(x_separation)
        close_x_separations[:, :][birds_outside_alert] = 0
        xvs[:] = np.add(xvs, np.sum(close_x_separations, 0))
        close_y_separations = np.copy(y_separation)
        close_y_separations[:, :][birds_outside_alert] = 0
        yvs[:] = np.add(yvs, np.sum(close_y_separations, 0))

        # Try to match speed with nearby boids
        birds_outside_formation = separation_distance_squared > formation_flying_distance
        x_velocity_difference = xvs[np.newaxis, :] - xvs[:, np.newaxis]
        y_velocity_difference = yvs[np.newaxis, :] - yvs[:, np.newaxis]
        close_x_formation = np.copy(x_velocity_difference)
        close_y_formation = np.copy(y_velocity_difference)
        close_x_formation[:, :][birds_outside_formation] = 0
        close_y_formation[:, :][birds_outside_formation] = 0
        xvs[:] = np.add(xvs, -1 * np.mean(close_x_formation, 0) * formation_flying_strength)
        yvs[:] = np.add(yvs, -1 * np.mean(close_y_formation, 0) * formation_flying_strength)

        # Update positions
        xs[:] = np.add(xs, xvs)
        ys[:] = np.add(ys, yvs)

    def animate(self,frame):
        self.update_boids(self.boids)
        scatter.set_offsets(zip(self.boids[0], self.boids[1]))

boidsobject = Boids()
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boidsobject.boids[0], boidsobject.boids[1])
anim = animation.FuncAnimation(figure, boidsobject.animate,
                                   frames=50, interval=50)

if __name__ == "__main__":

    plt.show()
