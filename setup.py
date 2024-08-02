from setuptools import setup, find_packages, Extension
import numpy


def configuration(parent_package='', top_path=None):
    config = {
        'name': 'geospatialtools',
        'version': '0.1.0',
        'description': 'A collection of geospatial tools including Fortran extensions.',
        'author': 'Your Name',
        'author_email': 'your.email@example.com',
        'packages': find_packages(),
        'ext_modules': [
            Extension('geospatialtools.terrain_tools_fortran',
                      ['src/planchon_2001.f90', 'src/terrain_tools.f90'],
                      extra_compile_args=['-fPIC', '-Wall', '-pedantic', '-O3']),
            Extension('geospatialtools.upscaling_tools_fortran',
                      ['src/upscaling_tools.f90'],
                      extra_compile_args=['-fPIC', '-Wall', '-pedantic', '-O3'])
        ],
        'package_dir': {'': 'libraries'},
        'install_requires': [
            'numpy>=' + numpy.__version__,
        ],
    }
    return config

if __name__ == '__main__':
    setup(**configuration())
