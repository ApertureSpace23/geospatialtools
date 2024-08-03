import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class CustomBuildExtCommand(build_ext):
    """Custom command to build Fortran files before building the Python extension."""
    def run(self):
        # Compile Fortran files into object files using gfortran
        os.system("gfortran -c -o src/planchon_2001.o src/planchon_2001.f90 -fPIC -O3 -Wall -pedantic")
        os.system("gfortran -c -o src/terrain_tools.o src/terrain_tools.f90 -fPIC -O3 -Wall -pedantic")
        os.system("gfortran -c -o src/upscaling_tools.o src/upscaling_tools.f90 -fPIC -O3 -Wall -pedantic")
        super().run()


setup(
    name='geospatialtools',
    version='0.1.0',
    packages=['geospatialtools'],
    package_dir={'geospatialtools': 'libraries'},
    ext_modules=[
        Extension('geospatialtools.terrain_tools_fortran',
                  sources=['src/planchon_2001.o', 'src/terrain_tools.o']),
        Extension('geospatialtools.upscaling_tools_fortran',
                  sources=['src/upscaling_tools.o'])
    ],
    cmdclass={
        'build_ext': CustomBuildExtCommand,
    },
)
