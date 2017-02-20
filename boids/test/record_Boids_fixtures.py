import yaml
from boids import Boids
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

boids = Boids()
before=deepcopy(boids.boids)
boids.separation(before[0],before[1])
alert_distance = 100
boids.fly_away_from_nearby_boids(boids.boids,boids.x_separation, boids.y_separation, boids.separation_distance_squared,alert_distance)
after= boids.boids
fixture={"before":np.array(before).tolist(),
         "after":np.array(after).tolist(),
         "alert_distance":alert_distance}
fixture_file=open("fixture_fly_away_from_nearby_boids.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

formation_flying_distance = 10000
formation_flying_strength = 0.125
before=deepcopy(boids.boids)
boids.separation(before[0],before[1])
boids.match_speed_with_nearby_boids(boids.boids, boids.separation_distance_squared,formation_flying_distance, formation_flying_strength )
after= boids.boids
fixture={"before":np.array(before).tolist(),
         "after":np.array(after).tolist(),
         "formation_flying_distance":formation_flying_distance,
         "formation_flying_strength":formation_flying_strength,
         "separation_distance_squared":np.array(boids.separation_distance_squared).tolist()}
fixture_file=open("fixture_match_speed_with_nearby_boids.yml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()