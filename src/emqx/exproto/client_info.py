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

from erlport.erlterms import Atom
from .until import to_binary


class ClientInfo:
    proto_name: str
    proto_version: str
    client_id: str
    username: str
    mountpoint: str
    keepalive: int

    def __init__(self, proto_name: str = '', proto_version: str = '', client_id: str = '',
                 username: str = '', mountpoint: str = '', keepalive: int = 0):
        self.proto_name = proto_name
        self.proto_version = proto_version
        self.client_id = client_id
        self.username = username
        self.mountpoint = mountpoint
        self.keepalive = keepalive

    def to_erlang_data_type(self) -> list:
        client_info_list = [
            (Atom(b"proto_name"), to_binary(self.proto_name)),
            (Atom(b"proto_ver"), to_binary(self.proto_version)),
            (Atom(b"clientid"), to_binary(self.client_id)),
            (Atom(b"username"), to_binary(self.username)),
            (Atom(b"mountpoint"), to_binary(self.mountpoint)),
            (Atom(b"keepalive"), to_binary(str(self.keepalive)))
        ]
        return client_info_list

    def __str__(self):
        string = f"ClientInfo{{ " \
            f"protoName={self.proto_name} " \
            f"protoVersion={self.proto_version} " \
            f"clientId={self.client_id} " \
            f"username={self.username} " \
            f"mountpoint={self.mountpoint} " \
            f"keepalive={self.keepalive} }}"
        return string
