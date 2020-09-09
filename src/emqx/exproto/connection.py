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

from erlport.erlterms import Pid
from .sock_type import SockType

class Sockname:
    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

class Peername:
    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port

class Connection:
    node = None
    idd = None
    serial = None
    creation = None
    pid = None

    def __init__(self, node=None, idd=None, serial=None, creation=None, pid=None):
        if pid:
            self.pid = pid
            self.node = pid.node
            self.idd = pid.idd
            self.serial = pid.serial
            self.creation = pid.creation
        else:
            self.node = node
            self.idd = idd
            self.serial = serial
            self.creation = creation


    def __str__(self):
        string = f"Connection{{ " \
            f"node={self.node}, " \
            f"id={self.idd}, " \
            f"serial={self.serial}, " \
            f"creation={self.creation}" \
            f"}}"
        return string


class ConnectionInfo:
    socket_type: str = ''
    peername_ip: str = ''
    peername_port: int = 0
    sockname: Sockname = None
    peername: Peername = None
    cert: str = ''
    cert_cn: str = ''
    cert_dn: str = ''

    def __init__(self, connInfo) -> 'ConnectionInfo':
        for info in connInfo:
            key = bytes.decode(info[0])
            if key == 'socktype':
                socktype = SockType()
                self.socket_type = socktype.get_socktype(info[1])
            elif key == 'peername':
                ip_tuple, port = info[1]
                peername_host = '.'.join(map(str, ip_tuple))
                peername_port = port
                self.peername = Peername(peername_host, peername_port)
            elif key == 'sockname':
                sockname_host = '.'.join(map(str, ip_tuple))
                sockname_port = port
                self.sockname = Sockname(sockname_host, sockname_port)
            elif key == 'peercert':
                cert_info = bytes.decode(info[1])
                if cert_info == 'nossl':
                    self.cert = 'nossl'
                else:
                    self.cert_cn = cert_info[0]
                    self.cert_dn = cert_info[0]
            else:
                continue

    def __str__(self):
        string = f"ConnectionInfo{{ " \
            f"socketType='{self.socket_type}', " \
            f"socknameIp='{self.sockname.host}', " \
            f"socknamePort='{self.sockname.port}', " \
            f"peernameIp='{self.peername.host}', " \
            f"peernamePort='{self.peername.port}', " \
            f"cert='{self.cert}', " \
            f"cert_cn='{self.cert_cn}', " \
            f"cert_dn='{self.cert_dn}'" \
            f"}}"
        return string
