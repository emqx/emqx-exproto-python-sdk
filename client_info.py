from erlport import Atom
from until import to_binary
class ClientInfo:
    proto_name: str = None
    proto_version: str = None
    client_id: str = None
    user_name: str = None
    mount_point: str = None
    keep_alive: str = None

    def __init__(self, proto_name: str, proto_version: str, client_id: str, user_name: str, mount_point: str, keep_alive: int):
        self.proto_name = proto_name
        self.proto_version = proto_version
        self.client_id = client_id
        self.user_name = user_name
        self.mount_point = mount_point
        self.keep_alive = keep_alive


    @staticmethod
    def to_erlang_data_type(client_info: ClientInfo) -> list:
        client_info_list = []
        client_info_list.append((Atom("proto_name"), to_binary(client_info.proto_name)))
        client_info_list.append((Atom("proto_ver"), to_binary(client_info.proto_version)))
        client_info_list.append((Atom("clientid"), to_binary(client_info.client_id)))
        client_info_list.append((Atom("username"), to_binary(client_info.user_name)))
        client_info_list.append((Atom("mountpoint"), to_binary(client_info.mount_point)))
        client_info_list.append((Atom("keepalive"), to_binary(client_info.keep_alive)))
        return client_info_list

    def __str__(self):
        s = f"ClientInfo{{\n protoName={self.proto_name}\n protoVersion={self.proto_version}\n clientId={self.client_id}\n userName={self.user_name}\n mountPoint={self.mount_point}\n keepAlive={self.keep_alive}\n }}"
        return s