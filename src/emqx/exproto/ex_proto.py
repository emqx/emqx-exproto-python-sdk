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

from typing import Tuple

from abstract_handler import AbstractExProtoHandler
from erlport.erlterms import Pid
from .connection import Connection, ConnectionInfo
from .message import Message


class ExProto:
    handler: AbstractExProtoHandler
    OK: int = 0

    def __init__(self, handler):
        self.handler = handler

    def init(self, conn: Pid, conn_info: list) -> Tuple[int, int]:
        connection = Connection(pid=conn)
        connection_info = ConnectionInfo(conn_info)
        self.handler.on_connect(connection, connection_info)
        state = 0
        return self.OK, state

    # TODO: state 是什么类型？ 2020/8/22
    def received(self, conn: Pid, data: bytes, state: any) -> any:
        connection = Connection(pid=conn)
        self.handler.on_received(connection, data, state)
        return state

    def terminated(self, conn: Pid, reason: str, state: any) -> None:
        connection = Connection(pid=conn)
        self.handler.on_terminated(connection, reason, state)
        return state

    def deliver(self, conn: Pid, msgs: list, state: any) -> Tuple[int, any]:
        connection = Connection(pid=conn)
        msg_list = Message.parse(msgs)
        self.handler.on_deliver(connection, msg_list)
        return self.OK, state
