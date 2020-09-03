from setuptools import setup, find_packages
import sys

requirements = ['emqx-erlport']

sys.path.insert(0, 'src')
__version__ = '0.1'

setup(
    name='emqx-exproto',
    version=__version__,
    description='',
    author='adek06',
    author_email='adek06@outlook.com',
    url='https://github.com/emqx/emqx-exproto-python-sdk',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    keywords='emqx',
    zip_safe=False,
    install_requires=requirements,
)
