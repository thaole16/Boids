from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture.yml')))
    boid_data=np.array(regression_data["before"])
    Boids().update_boids(boid_data)
    after_data = np.array(regression_data["after"])
    for after,before in zip(after_data,boid_data):
        for after_value,before_value in zip(after,before):
            np.testing.assert_almost_equal(after_value,before_value)