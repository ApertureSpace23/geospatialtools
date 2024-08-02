import setuptools
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
import os
import subprocess

class CustomBuildExtCommand(build_ext):
    """Custom command to compile Fortran files using f2py before building the package."""
    def run(self):
        # Compile Fortran modules
        f2py_cmds = [
            ('terrain_tools_fortran', ['src/planchon_2001.f90', 'src/terrain_tools.f90']),
            ('upscaling_tools_fortran', ['src/upscaling_tools.f90'])
        ]
        for mod_name, sources in f2py_cmds:
            try:
                # You can customize the f2py command according to your compilation preferences
                subprocess.check_call(['f2py', '-c', '-m', mod_name] + sources + ['-fPIC', '-Wall', '-pedantic', '-O3'])
            except subprocess.CalledProcessError as e:
                raise RuntimeError("f2py failed to compile: " + ' '.join(e.cmd))
        # Call the original build_ext command
        super().run()


setup(
    name="geospatialtools",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A collection of geospatial tools.",
    packages=find_packages(where='libraries'),  # Look for packages in 'libraries' directory
    package_dir={'': 'libraries'},  # Set the root directory for packages to 'libraries'
    install_requires=[
        "numpy>=1.26.4"  # ensure dependencies are listed correctly
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
