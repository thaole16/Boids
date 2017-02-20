import yaml
import boids.boids.boids
from copy import deepcopy
before=deepcopy(boids.boids.boids)
boids.boids.update_boids(boids.boids.boids)
after= boids.boids.boids
fixture={"before":before,"after":after}
fixture_file=open("fixture.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
