from boids import Boids
from matplotlib import pyplot as plt
from argparse import ArgumentParser
import yaml
import ConfigParser

def main():
    parser = ArgumentParser(description="Boid Flocking Modelling")
    parser.add_argument('--config', '-c', default='config.yml')
    args = parser.parse_args()

    with open(args.config, 'r') as ymlfile:
        configdata = yaml.load(ymlfile)
        boid_count = configdata['Boids_Setup']['boid_count']
        x_positions = configdata['Boids_Setup']['x_positions']
        y_positions = configdata['Boids_Setup']['y_positions']
        x_velocities = configdata['Boids_Setup']['x_velocities']
        y_velocities = configdata['Boids_Setup']['y_velocities']

        move_to_middle_strength = configdata['Flock_Dynamics']['move_to_middle_strength']
        alert_distance = configdata['Flock_Dynamics']['alert_distance']
        formation_flying_distance = configdata['Flock_Dynamics']['formation_flying_distance']
        formation_flying_strength = configdata['Flock_Dynamics']['formation_flying_strength']

        xlim = configdata['Axis_Limits']['xlim']
        ylim = configdata['Axis_Limits']['ylim']

        frames = configdata['Animation']['frames']
        interval = configdata['Animation']['interval']

        boidsobject = Boids(boid_count = boid_count,
                 x_positions = x_positions,
                 y_positions = y_positions,
                 x_velocities = x_velocities,
                 y_velocities = y_velocities,
                 move_to_middle_strength=move_to_middle_strength,
                 alert_distance = alert_distance,
                 formation_flying_distance = formation_flying_distance,
                 formation_flying_strength = formation_flying_strength)
        boidsobject.model(xlim=xlim, ylim=ylim, frames=frames, interval=interval)



