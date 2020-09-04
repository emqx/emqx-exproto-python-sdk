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

class ConstantsMeta(type):
    def __setattr__(self, key, value):
        raise AttributeError(f"you can't set this attribute: {key} = {value}")


class BaseConstant(metaclass=ConstantsMeta):
    ...


class SockType(BaseConstant):
    TCP = 'tcp'
    TLS = 'tls'
    UDP = 'udp'
    DTLS = 'dtls'

    def get_socktype(self, atom):
        sock_type = bytes.decode(atom)
        if sock_type == 'tcp':
            return self.TCP
        elif sock_type == 'tls':
            return self.TLS
        elif sock_type == 'udp':
            return self.UDP
        elif sock_type == 'dtls':
            return self.DTLS
        else:
            return None
