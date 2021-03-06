from boids import Boids
from argparse import ArgumentParser
import yaml
import os

def main():
    _ROOT = os.path.abspath(os.path.dirname(__file__))
    defaultconfig = os.path.join(_ROOT, 'config.yml')
    parser = ArgumentParser(description="Boid Flocking Modelling")
    parser.add_argument('--config', default=defaultconfig, help="Configuration file", metavar="FILE")
    parser.add_argument('--saveto', help="Filename to save animation", metavar="FILE")
    args = parser.parse_args()

    try:
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

            saveto = args.saveto #works even if it is None

            boidsobject = Boids(boid_count=boid_count,
                                x_positions=x_positions,
                                y_positions=y_positions,
                                x_velocities=x_velocities,
                                y_velocities=y_velocities,
                                move_to_middle_strength=move_to_middle_strength,
                                alert_distance=alert_distance,
                                formation_flying_distance=formation_flying_distance,
                                formation_flying_strength=formation_flying_strength)
            boidsobject.model(xlim=xlim,
                              ylim=ylim,
                              frames=frames,
                              interval=interval,
                              savefile=saveto)
    except IOError as error:
        print('IOError: No such config file')
    except KeyError as error:
        print('KeyError: Missing parameters in config file')




