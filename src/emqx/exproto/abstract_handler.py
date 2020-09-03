from abc import ABCMeta, abstractmethod

from emqx.erlport import erlang
from emqx.erlport.erlterms import Atom
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
        erlang.call(Atom(b'emqx_exproto'), Atom(b'send'), (connection.pid, data))

    def terminate(self, connection: Connection):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'close'), (connection.pid))

    def register(self, connection: Connection, client_info: ClientInfo):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'register'), (connection.pid, client_info.to_erlang_data_type()))

    def publish(self, connection: Connection, message: Message):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'publish'), (connection.pid, message.to_erlang_data_type()))

    def subscribe(self, connection: Connection, topic: str, qos: int):
        erlang.call(Atom(b'emqx_exproto'), Atom(b'subscribe'), (connection.pid, bytes(topic), qos))