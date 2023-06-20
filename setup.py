from __future__ import print_function
from setuptools import setup, Command
from setuptools.command.install import install

import os
import sys
import shutil
import subprocess as sp

# monkey patch because setuptools entry_points are slow as fuck
# https://github.com/ninjaaron/fast-entry_points
import fastentrypoints

HERE = os.path.abspath(os.path.dirname(__file__))


def python_below_34():
    return sys.version_info[0] < 3 or sys.version_info[1] < 4

# yapf: disable
setup(
    name="evo",
    version=open("evo/version").read(),
    description="Python package for the evaluation of odometry and SLAM",
    author="Antoni Rosinol, Michael Grupp",
    author_email="arosinol@mit.edu,",
    url="https://github.com/sphillips-bdai/evo_kimera.git",
    license="GPLv3",
    keywords=[
        "SLAM", "odometry", "trajectory", "evaluation", "metric",
        "vision", "laser", "visual", "robotics"
    ],
    packages=["evo", "evo.core", "evo.tools"],
    package_data={"evo": ["version", "LICENSE"]},
    entry_points={"console_scripts": [
        "evo_evaluation=evo.entry_points:evaluation",
        "evo_ape=evo.entry_points:ape",
        "evo_rpe=evo.entry_points:rpe",
        "evo_traj=evo.entry_points:traj",
        "evo_res=evo.entry_points:res",
        "evo_config=evo.main_config:main",
        "evo_fig=evo.main_fig:main",
        "evo_ipython=evo.main_ipython:main",
        "evo=evo.main_evo:main"
    ]},
    zip_safe=False,
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "pandas",
        "seaborn",
        "natsort",
        "argcomplete",
        "colorama",
        "pygments",
        "pyyaml"
        #jupyter
    ] + (["enum34"] if python_below_34() else []),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython"
    ]
)
# yapf: enable
