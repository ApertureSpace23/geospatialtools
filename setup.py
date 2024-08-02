from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import numpy

class BuildExt(build_ext):
    def build_extensions(self):
        self.include_dirs.append(numpy.get_include())
        super().build_extensions()

# Define a simple extension for demonstration, replace with your actual Fortran compilation
extensions = [
    Extension(
        'geospatialtools.terrain_tools_fortran',
        sources=['src/planchon_2001.f90', 'src/terrain_tools.f90'],
        extra_compile_args=['-fPIC', '-Wall', '-pedantic', '-O3']
    ),
    Extension(
        'geospatialtools.upscaling_tools_fortran',
        sources=['src/upscaling_tools.f90'],
        extra_compile_args=['-fPIC', '-Wall', '-pedantic', '-O3']
    )
]

setup(
    name='geospatialtools',
    version='0.1',
    packages=['geospatialtools'],
    ext_modules=extensions,
    cmdclass={'build_ext': BuildExt}
)
