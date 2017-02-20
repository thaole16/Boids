from boids import Boids
from nose.tools import assert_almost_equal,assert_equals, assert_raises
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=np.array(regression_data["before"])
    Boids().update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_Boids():
    boidobject = Boids()
    assert_equals(boidobject.boids_x.size, 50)
    assert_equals(boidobject.boids_y.size, 50)
    assert_equals(boidobject.boid_x_velocities.size, 50)
    assert_equals(boidobject.boid_y_velocities.size, 50)

    boidobject = Boids(boid_count = 2)
    assert_equals(boidobject.boids_x.size, 2)
    assert_equals(boidobject.boids_y.size, 2)
    assert_equals(boidobject.boid_x_velocities.size, 2)
    assert_equals(boidobject.boid_y_velocities.size, 2)

    with assert_raises(ValueError):
        boidobject = Boids(boid_count = -2)
