from setuptools import setup, find_packages

setup(
    name="Boids",

    version="0.1.1",

    description="Boid flocking",
    long_description=open('README.md').read(),

    url='https://github.com/thaole16/Boids',

    author='MPHYG001, Thao Le',
    author_email='thao.le.16@ucl.ac.uk',

    packages=find_packages(exclude=['*test','docs']),

    entry_points={'console_scripts': ['boidsflock=boids:main']},

    install_requires=['argparse','numpy','matplotlib','nose','pyyaml','mock'],

    license="MIT",

    classifiers=[
        'License :: MIT License',
        'Intended Audience :: MPHYG001 Markers',
        'Programming Language :: Python :: 2.7',

    ]
)