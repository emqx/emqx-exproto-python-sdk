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

from erlport.erlterms import Pid
from erlport import erlang
from .connection import Connection, ConnectionInfo
from .message import Message

import emqx.exproto.driver as driver


OK = 0
ERROR = 1

##--------------------------------------------------------------------
## Connection level

def init(conn, conninfo):
    connection = Connection(pid=conn)
    connection_info = ConnectionInfo(conninfo)
    driver.exproto_driver.on_connect(connection, connection_info)
    state = 0
    return (OK, state)

def received(conn, data, state):
    connection = Connection(pid=conn)
    driver.exproto_driver.on_received(connection, data, state)
    return (OK, state+1)

def terminated(conn, reason, state):
    connection = Connection(pid=conn)
    driver.exproto_driver.on_terminated(connection, reason, state)
    return

##--------------------------------------------------------------------
## Protocol/Session level

def deliver(conn, msgs, state):
    connection = Connection(pid=conn)
    msg_list = Message.parse(msgs)
    driver.exproto_driver.on_deliver(connection, msg_list)
    return (OK, state+1)
