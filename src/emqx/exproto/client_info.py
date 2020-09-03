from emqx.erlport.erlterms import Atom
from .until import to_binary


class ClientInfo:
    proto_name: str
    proto_version: str
    client_id: str
    user_name: str
    mount_point: str
    keep_alive: int

    def __init__(self, proto_name: str = '', proto_version: str = '', client_id: str = '',
                 user_name: str = '', mount_point: str = '', keep_alive: int = 0):
        self.proto_name = proto_name
        self.proto_version = proto_version
        self.client_id = client_id
        self.user_name = user_name
        self.mount_point = mount_point
        self.keep_alive = keep_alive

    def to_erlang_data_type(self) -> list:
        client_info_list = [
            (Atom(b"proto_name"), to_binary(self.proto_name)),
            (Atom(b"proto_ver"), to_binary(self.proto_version)),
            (Atom(b"clientid"), to_binary(self.client_id)),
            (Atom(b"username"), to_binary(self.user_name)),
            (Atom(b"mountpoint"), to_binary(self.mount_point)),
            (Atom(b"keepalive"), to_binary(str(self.keep_alive)))
        ]
        return client_info_list

    def __str__(self):
        string = f"ClientInfo{{\n " \
            f"protoName={self.proto_name}\n " \
            f"protoVersion={self.proto_version}\n " \
            f"clientId={self.client_id}\n " \
            f"userName={self.user_name}\n " \
            f"mountPoint={self.mount_point}\n " \
            f"keepAlive={self.keep_alive}\n }}"
        return string
