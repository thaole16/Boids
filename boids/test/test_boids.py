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

def test_fly_towards_the_middle():
    data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture_fly_towards_the_middle.yml')))
    boid_data_before=np.array(data["before"])
    boid_data_after = np.array(data["after"])
    move_to_middle_strength = data["move_to_middle_strength"]

    boids = Boids()
    boids.boids = boid_data_before
    boids.fly_towards_the_middle(boid_data_before, move_to_middle_strength)

    np.testing.assert_array_almost_equal(boids.boids,boid_data_after)

def test_separation():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture_separation.yml')))
    xcoords = np.array(data["xcoords"])
    ycoords = np.array(data["ycoords"])
    x_separation = np.array(data["x_separation"])
    y_separation = np.array(data["y_separation"])
    separation_distance_squared = np.array(data["separation_distance_squared"])
    boids = Boids(boid_count = 2)
    boids.separation(xcoords, ycoords)

    np.testing.assert_array_almost_equal(boids.x_separation,x_separation)
    np.testing.assert_array_almost_equal(boids.y_separation, y_separation)
    np.testing.assert_array_almost_equal(boids. separation_distance_squared,  separation_distance_squared)

def test_fly_away_from_nearby_boids():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture_fly_away_from_nearby_boids.yml')))
    boid_data_before = np.array(data["before"])
    boid_data_after = np.array(data["after"])
    alert_distance = data["alert_distance"]
    boids = Boids()
    boids.boids = boid_data_before
    boids.separation(boid_data_before[0],boid_data_before[1])

    boids.fly_away_from_nearby_boids(boids.boids, boids.x_separation, boids.y_separation,
                                     boids.separation_distance_squared, alert_distance)
    np.testing.assert_array_almost_equal(boids.boids, boid_data_after)

def test_match_speed_with_nearby_boids():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture_match_speed_with_nearby_boids.yml')))
    boid_data_before = np.array(data["before"])
    boid_data_after = np.array(data["after"])
    formation_flying_distance = data["formation_flying_distance"]
    formation_flying_strength = data["formation_flying_strength"]
    separation_distance_squared = np.array(data["separation_distance_squared"])

    boids = Boids()
    boids.boids = boid_data_before
    boids.match_speed_with_nearby_boids(boids.boids, separation_distance_squared,formation_flying_distance,formation_flying_strength)
    np.testing.assert_array_almost_equal(boids.boids, boid_data_after)
