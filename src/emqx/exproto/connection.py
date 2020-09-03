from .sock_type import SockType


class Connection:
    node = None
    idd = None
    serial = None
    creation = None
    pid = None

    def __init__(self, node=None, idd=None, serial=None, creation=None, pid=None):
        if pid:
            self.pid = pid
            self.node = pid.node
            self.idd = pid.idd
            self.serial = pid.serial
            self.creation = pid.creation
        else:
            self.node = node
            self.idd = idd
            self.serial = serial
            self.creation = creation

    def __str__(self):
        string = f"Connection{{ \n " \
            f"node={self.node} \n " \
            f"id={self.idd} \n " \
            f"serial={self.serial} \n " \
            f"creation={self.creation} \n" \
            f"}}"
        return string


class ConnectionInfo:
    socket_type: str = ''
    peername_ip: str = ''
    peername_port: int = 0
    socket_ip: str = ''
    socket_name: int = 0
    cert: str = ''
    cert_cn: str = ''
    cert_dn: str = ''

    def __init__(self, connInfo) -> 'ConnectionInfo':
        for info in connInfo:
            key = bytes.decode(info[0])
            if key == 'socktype':
                socktype = SockType()
                self.socket_type = socktype.get_socktype(info[1])
            elif key == 'peername':
                ip_tuple, port = info[1]
                self.peername_ip = '.'.join(map(str, ip_tuple))
                self.peername_port = port
            elif key == 'sockname':
                self.socket_ip = '.'.join(map(str, ip_tuple))
                self.socket_name = port
            elif key == 'peercert':
                cert_info = bytes.decode(info[1])
                if cert_info == 'nossl':
                    self.cert = 'nossl'
                else:
                    self.cert_cn = cert_info[0]
                    self.cert_dn = cert_info[0]
            else:
                continue

    def __str__(self):
        string = f"EmqxConnectionInfo{{\n " \
            f"socketType='{self.socket_type}'\n " \
            f"socketIP='{self.socket_ip}'\n " \
            f"socketPort='{self.socket_name}' \n " \
            f"peerNameIp='{self.peername_ip}' \n " \
            f"peerNamePort='{self.peername_port}' \n " \
            f"cert='{self.cert}' \n " \
            f"cert_cn='{self.cert_cn}' \n " \
            f"cert_dn='{self.cert_dn}'\n" \
            f"}}"
        return string
