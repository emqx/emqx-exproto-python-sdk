from abc import ABCMeta, abstractmethod

from emqx.erlport import erlang
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
    def on_terminated(self, connection: Connection, reason: str, state: any) -> int:
        ...

    @abstractmethod
    def on_deliver(self, connection: Connection, message_list: list):
        ...

    def send(self, connection: Connection, data: bytes):
        erlang.call('emqx_exproto', 'send', (connection.pid, data), 5000)

    def terminate(self, connection: Connection):
        erlang.call('emqx_exproto', 'close', (connection.pid), 5000)

    def register(self, connection: Connection, client_info: ClientInfo):
        erlang.call('emqx_exproto', 'register', (connection.pid, client_info.to_erlang_data_type()), 5000)

    def publish(self, connection: Connection, message: Message):
        erlang.call('emqx_exproto', 'publish', (connection.pid, message.to_erlang_data_type()), 5000)

    def subscribe(self, connection: Connection, topic: str, qos: int):
        erlang.call('emqx_exproto', 'subscribe', (connection.pid, bytes(topic), qos), 5000)