from emqx.erlport.erlterms import Atom
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
        string = f"ClientInfo{{\n " \
            f"protoName={self.proto_name}\n " \
            f"protoVersion={self.proto_version}\n " \
            f"clientId={self.client_id}\n " \
            f"username={self.username}\n " \
            f"mountpoint={self.mountpoint}\n " \
            f"keepalive={self.keepalive}\n }}"
        return string
