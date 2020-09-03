from setuptools import setup, find_packages
import sys

requirements = []

sys.path.insert(0, 'src')
from emqx.exproto import __version__

setup(
    name='emqx-exproto',
    version=__version__,
    description='',
    author='adek06',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    keywords='emqx',
    zip_safe=False,
    install_requires=[],
)
