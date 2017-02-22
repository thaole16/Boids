"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Boids(object):

    def __init__(self,
                 boid_count = 50,
                 x_positions = [-450, 50.0],
                 y_positions = [300.0, 600.0],
                 x_velocities = [0, 10.0],
                 y_velocities = [-20.0, 20.0],
                 move_to_middle_strength=0.01,
                 alert_distance = 100,
                 formation_flying_distance = 10000,
                 formation_flying_strength = 0.125):

        self.boid_count = boid_count
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength

        self.boids_x = np.random.uniform(size=boid_count,*x_positions)
        self.boids_y = np.random.uniform(size=boid_count,*y_positions)
        self.positions = np.stack((self.boids_x,self.boids_y))
        self.boid_x_velocities = np.random.uniform(size=boid_count, *x_velocities)
        self.boid_y_velocities = np.random.uniform(size=boid_count, *y_velocities)
        self.velocities = np.stack((self.boid_x_velocities,self.boid_y_velocities))

        self.boids = (self.positions, self.velocities)

    def fly_towards_the_middle(self,boids,move_to_middle_strength = 0.01):
        positions_x, positions_y, velocities_x, velocities_y = boids
        # Fly towards the middle
        x_move_to_middle = (np.mean(positions_x) - positions_x) * move_to_middle_strength
        y_move_to_middle = (np.mean(positions_y) - positions_y) * move_to_middle_strength
        velocities_x[:] = np.add(velocities_x, x_move_to_middle)
        velocities_y[:] = np.add(velocities_y, y_move_to_middle)

    def separation(self,xcoords, ycoords):
        self.x_separation = xcoords[np.newaxis, :] - xcoords[:, np.newaxis]
        self.y_separation = ycoords[np.newaxis, :] - ycoords[:, np.newaxis]
        self.separation_distance_squared = self.x_separation ** 2 + self.y_separation ** 2

    def fly_away_from_nearby_boids(self,boids,x_separation, y_separation, separation_distance_squared,alert_distance=100):
        positions_x, positions_y, velocities_x, velocities_y = boids
        birds_outside_alert = separation_distance_squared > alert_distance
        close_x_separations = np.copy(x_separation)
        close_x_separations[:, :][birds_outside_alert] = 0
        velocities_x[:] = np.add(velocities_x, np.sum(close_x_separations, 0))
        close_y_separations = np.copy(y_separation)
        close_y_separations[:, :][birds_outside_alert] = 0
        velocities_y[:] = np.add(velocities_y, np.sum(close_y_separations, 0))

    def match_speed_with_nearby_boids(self,boids,
                                      separation_distance_squared,
                                      formation_flying_distance = 10000,
                                      formation_flying_strength = 0.125):
        positions_x, positions_y, velocities_x, velocities_y = boids
        birds_outside_formation = separation_distance_squared > formation_flying_distance
        x_velocity_difference = velocities_x[np.newaxis, :] - velocities_x[:, np.newaxis]
        y_velocity_difference = velocities_y[np.newaxis, :] - velocities_y[:, np.newaxis]
        close_x_formation = np.copy(x_velocity_difference)
        close_y_formation = np.copy(y_velocity_difference)
        close_x_formation[:, :][birds_outside_formation] = 0
        close_y_formation[:, :][birds_outside_formation] = 0
        velocities_x[:] = np.add(velocities_x, -1 * np.mean(close_x_formation, 0) * formation_flying_strength)
        velocities_y[:] = np.add(velocities_y, -1 * np.mean(close_y_formation, 0) * formation_flying_strength)

    def update_boids(self, boids):
        positions_x, positions_y, velocities_x, velocities_y = boids
        # Fly towards the middle
        self.fly_towards_the_middle(boids,self.move_to_middle_strength)

        #calculate the separations
        self.separation(positions_x,positions_y)

        # Fly away from nearby boids
        self.fly_away_from_nearby_boids(boids,
                                        self.x_separation,
                                        self.y_separation,
                                        self.separation_distance_squared,
                                        self.alert_distance)

        # Try to match speed with nearby boids
        self.match_speed_with_nearby_boids(boids, self.separation_distance_squared,
                                           self.formation_flying_distance,
                                           self.formation_flying_strength)

        # Update positions
        positions_x[:] = np.add(positions_x, velocities_x)
        positions_y[:] = np.add(positions_y, velocities_y)

    def animate(self,frame):
        self.update_boids(self.boids)
        self.scatter.set_offsets(zip(self.boids_x, self.boids_y))

    def model(self, xlim=(-500, 1500), ylim=(-500, 1500), frames=50, interval=50):
        colors = np.random.rand(self.boid_count)
        boidsize = np.pi * (2 * np.random.rand(self.boid_count)+2) ** 2

        figure = plt.figure()
        axes = plt.axes(xlim=xlim, ylim=ylim)
        self.scatter = axes.scatter(self.boids_x, self.boids_y,
                                    s=boidsize, c=colors, alpha=0.5, edgecolors = None)
        anim = animation.FuncAnimation(figure, self.animate,
                                       frames=frames, interval=interval)
        plt.xlabel('x (arbitrary units)')
        plt.ylabel('y (arbitrary units)')
        plt.title("Boids a'Flocking")

        plt.show()

if __name__ == "__main__":
    boidsobject = Boids()
    boidsobject.model()
