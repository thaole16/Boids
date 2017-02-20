import yaml
from boids.boids import Boids
from copy import deepcopy
import numpy as np

boids = Boids()
before=deepcopy(boids.boids)
move_to_middle = 0.01
boids.fly_towards_the_middle(boids.boids,move_to_middle)
after= boids.boids
fixture={"before":np.array(before).tolist(),"after":np.array(after).tolist(), "move_to_middle_strength":move_to_middle}
fixture_file=open("fixture_fly_towards_the_middle.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()