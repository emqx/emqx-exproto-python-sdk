from emqx.exproto.abstract_handler import AbstractExProtoHandler
from emqx.exproto.connection import Connection, ConnectionInfo


class SdkDemo(AbstractExProtoHandler):
    def on_connect(self, connection: Connection, connection_info: ConnectionInfo):
        print(connection)
        print(connection_info)

    def on_received(self, connection: Connection, data: bytes, state: any):
        print(connection)
        print(bytes.decode(data))

    def on_terminated(self, connection: Connection, reason: str, state: any):
        print(connection)
        print(reason)

    def on_deliver(self, connection: Connection, message_list: list):
        print(connection)
        for message in message_list:
            print(message)
