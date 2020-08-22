from abc import ABCMeta, abstractmethod

from connection import Connection, ConnectionInfo


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
