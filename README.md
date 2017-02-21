==========
Boids
==========

> The aggregate motion of a flock of birds, a herd of land animals, or a school of fish is a beautiful and familiar
part of the natural world... The aggregate motion of the simulated flock is created by a distributed behavioral
model much like that at work in a natural flock; the birds choose their own course. Each simulated bird is implemented
as an independent actor that navigates according to its local perception of the dynamic environment, the laws of
simulated physics that rule its motion, and a set of behaviors programmed into it... The aggregate motion of the
simulated flock is the result of the dense interaction of the relatively simple behaviors of the individual
 simulated birds.

*Reynolds, C.W., Computer Graphics 21 4 (1987), pp 25-34*

Boids is a basic model of the flocking of birds, based on three rules that govern an individual bird's flight
trajectory, which ultimiately leads to overall emergent behaviour of the flock:

1. Birds tend to fly towards the middle of the overall flock.
2. Birds don't want to fly too close to neighbouring birds.
3. Birds tend to match flight speed with nearby birds.

The original boids code is taken from the
[bad-boids github repository](https://github.com/jamespjh/bad-boids)
, which in turn comes from the
[UCL Research Software Engineering course](http://github-pages.ucl.ac.uk/rsd-engineeringcourse/ch05construction/10boids.html)

Requirements
=========================

This package runs on Python 2.7.

Installation Instructions
=========================

To install via pip:

    pip install git+https://github.com/thaole16/greengraph.git

To install directly:

1. Download the package
2. Navigate to the Boids folder where setup.py is located
3. Run:
    python setup.py install

If you want to run the testing, also run:
    python setup.py test

Typical Usage
=============

This package is called using __boidsflock__.

To use, a YAML configuration file is required. A default one is given (config.yml). For example:

    boidsflock --config config.yml

Configuration Parameters
========================
The yaml configuration file is a nested dictionary (with default values for example):

```yaml
Boids_Setup:
  boid_count: 50
  x_positions: [-450,50.0]
  y_positions: [300.0,600.0]
  x_velocities: [0, 10.0]
  y_velocities: [-20.0, 20.0]
Flock_Dynamics:
  move_to_middle_strength: 0.01
  alert_distance: 100
  formation_flying_distance: 10000
  formation_flying_strength: 0.125
Axis_Limits:
  xlim: [-500, 1500]
  ylim: [-500, 1500]
Animation:
  frames: 50
  interval: 50
 ```