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

from abc import ABCMeta, abstractmethod

from erlport import erlang
from erlport.erlterms import Atom, Pid
from .connection import Connection, ConnectionInfo
from .client_info import ClientInfo
from .message import Message

class AbstractExProtoHandler(metaclass=ABCMeta):

    @abstractmethod
    def on_connect(self, connection: Connection, connection_info: ConnectionInfo):
        ...

    @abstractmethod
    def on_received(self, connection: Connection, data: bytes, state: any) -> any:
        ...

    @abstractmethod
    def on_terminated(self, connection: Connection, reason: bytes, state: any) -> int:
        ...

    @abstractmethod
    def on_deliver(self, connection: Connection, message_list: list):
        ...

    def send(self, connection: Connection, data: bytes):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'send'), [connection.pid, data])

    def terminate(self, connection: Connection):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'close'), [connection.pid])

    def register(self, connection: Connection, client_info: ClientInfo):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'register'), [connection.pid, client_info.to_erlang_data_type()])

    def publish(self, connection: Connection, message: Message):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'publish'), [connection.pid, message.to_erlang_data_type()])

    def subscribe(self, connection: Connection, topic: str, qos: int):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'subscribe'), [connection.pid, bytes(topic), qos])
