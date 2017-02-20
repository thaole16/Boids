import yaml
from boids import Boids
from copy import deepcopy
import numpy as np

boids = Boids()
before= np.array(deepcopy(boids.boids)).tolist()
boids.update_boids(boids.boids)
after= np.array(boids.boids).tolist()
fixture={"before":before,"after":after}
fixture_file=open("fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
