"""
Unit testing for the functions in the Boids class
"""

from boids import Boids
from nose.tools import assert_equals, assert_raises
import os
import yaml
import numpy as np
from mock import patch

def test_Boids():

    for boid_count in (10,2):
        boidobject = Boids(boid_count=boid_count)
        assert_equals(boidobject.boids_x.size, boid_count)
        assert_equals(boidobject.boids_y.size, boid_count)
        assert_equals(boidobject.boid_x_velocities.size, boid_count)
        assert_equals(boidobject.boid_y_velocities.size, boid_count)

    with assert_raises(ValueError):
        boidobject = Boids(boid_count = -2)

def test_fly_towards_the_middle():
    data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture_fly_towards_the_middle.yml')))
    boid_data_before=np.array(data["before"])
    boid_data_after = np.array(data["after"])
    move_to_middle_strength = data["move_to_middle_strength"]

    boids = Boids()
    boids.boids = boid_data_before
    boids.fly_towards_the_middle(boids.boids, move_to_middle_strength)

    np.testing.assert_array_almost_equal(boids.boids,boid_data_after)

def test_separation():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture_separation.yml')))
    xcoords = np.array(data["xcoords"])
    ycoords = np.array(data["ycoords"])
    x_separation = np.array(data["x_separation"])
    y_separation = np.array(data["y_separation"])
    separation_distance_squared = np.array(data["separation_distance_squared"])
    boids = Boids(boid_count = data["boid_count"])
    calc_separations, calc_separation_distance_squared = boids.separation((xcoords, ycoords))

    np.testing.assert_array_almost_equal(calc_separations,(x_separation,y_separation))
    np.testing.assert_array_almost_equal( calc_separation_distance_squared,  separation_distance_squared)

def test_fly_away_from_nearby_boids():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture_fly_away_from_nearby_boids.yml')))
    boid_data_before = np.array(data["before"])
    boid_data_after = np.array(data["after"])
    alert_distance = data["alert_distance"]
    boids = Boids()
    boids.boids = boid_data_before

    boids.fly_away_from_nearby_boids(boids.boids, alert_distance)
    np.testing.assert_array_almost_equal(boids.boids, boid_data_after)

def test_match_speed_with_nearby_boids():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','fixture_match_speed_with_nearby_boids.yml')))
    boid_data_before = np.array(data["before"])
    boid_data_after = np.array(data["after"])
    formation_flying_distance = data["formation_flying_distance"]
    formation_flying_strength = data["formation_flying_strength"]

    boids = Boids()
    boids.boids = boid_data_before
    boids.match_speed_with_nearby_boids(boids.boids, formation_flying_distance,formation_flying_strength)
    np.testing.assert_array_almost_equal(boids.boids, boid_data_after)

def test_update_boids():
    data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures', 'fixture_update_boids_only.yml')))
    boid_data_before = np.array(data["before"])
    boid_data_after = np.array(data["after"])
    boid_count = data["boid_count"]
    boids = Boids(boid_count = boid_count)
    boids.boids = boid_data_before
    with patch.object(boids,'fly_towards_the_middle') as mocked1:
        with patch.object(boids, 'fly_away_from_nearby_boids') as mocked2:
            with patch.object(boids,'match_speed_with_nearby_boids') as mocked3:
                boids.update_boids(boids.boids)
                np.testing.assert_almost_equal(boids.boids, boid_data_after)

