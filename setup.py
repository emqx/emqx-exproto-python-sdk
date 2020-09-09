# Copyright (c) 2020 EMQ Technologies Co., Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import sys

requirements = []

sys.path.insert(0, 'src')
__version__ = '0.1.4'


setup(
    name='emqx-exproto-sdk',
    version=__version__,
    description='The Python SDK for emqx-exproto',
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
