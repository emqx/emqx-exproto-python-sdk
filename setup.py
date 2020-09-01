from setuptools import setup
from emqx.exproto import __version__

requirements = ['erlport']

setup(
    name='emqx-exproto',
    version=__version__,
    description='',
    author='adek06',
    packages='',
    keywords='emqx',
    zip_safe=False,
    install_requires=requirements,
)