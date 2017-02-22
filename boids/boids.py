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
        (positions, velocities) = boids
        middle = np.mean(positions,1)
        move_to_middle = (middle[:,np.newaxis] - positions) * move_to_middle_strength
        velocities += move_to_middle

    def separation(self, coords):
        separations = np.array(coords)[:,np.newaxis,:] - np.array(coords)[:,:,np.newaxis]
        separation_distance_squared = separations[0,:,:] ** 2 + separations[1,:,:] ** 2
        return separations, separation_distance_squared

    def fly_away_from_nearby_boids(self,boids,alert_distance=100):
        (positions, velocities) = boids
        separations, separation_distance_squared = self.separation(positions)
        birds_outside_alert = separation_distance_squared > alert_distance
        close_separations = np.copy(separations)
        close_separations[0,:,:][birds_outside_alert] = 0 #x positions
        close_separations[1,:,:][birds_outside_alert] = 0 #y positions
        velocities += np.sum(close_separations,1)

    def match_speed_with_nearby_boids(self,boids,
                                      formation_flying_distance=10000,
                                      formation_flying_strength=0.125):
        (positions, velocities) = boids
        separations, separation_distance_squared = self.separation(positions)
        (velocities_x, velocities_y) = np.split(velocities, 2)
        birds_outside_formation = separation_distance_squared > formation_flying_distance
        velocity_difference = velocities[:, np.newaxis, :] - velocities[:,:, np.newaxis]
        close_formation = np.copy(velocity_difference)
        close_formation[0, :, :][birds_outside_formation] = 0
        close_formation[1,:, :][birds_outside_formation] = 0
        velocities += -1 * np.mean(close_formation, 1) * formation_flying_strength

    def update_boids(self, boids):
        (positions,velocities) = boids

        # Fly towards the middle
        self.fly_towards_the_middle(boids,self.move_to_middle_strength)

        # Fly away from nearby boids
        self.fly_away_from_nearby_boids(boids, self.alert_distance)

        # Try to match speed with nearby boids
        self.match_speed_with_nearby_boids(boids, self.formation_flying_distance, self.formation_flying_strength)

        # Update positions
        positions += velocities

    def animate(self,frame):
        self.update_boids(self.boids)
        (positions,velocities) = self.boids
        self.scatter.set_offsets(np.transpose(positions))

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
