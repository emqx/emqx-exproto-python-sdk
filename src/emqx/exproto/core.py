from typing import Tuple

from emqx.erlport.erlterms import Pid
from emqx.erlport import erlang
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
