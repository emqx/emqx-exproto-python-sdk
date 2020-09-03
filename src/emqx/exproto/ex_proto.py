from typing import Tuple

from abstract_handler import AbstractExProtoHandler
from emqx.erlport.erlterms import Pid
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
