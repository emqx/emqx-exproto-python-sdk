from erlport import Atom
from erlport import erlang
from sock_type import SockType

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
        s = f"Connection{{ \n node={self.node} \n id={self.idd} \n serial={self.serial} \n creation={self.creation} \n}}"
        return s

class ConnectionInfo:

    socket_type: str = None
    peername_ip: str = None
    peername_port: int = None
    socket_ip: str = None
    socket_name: int  = None
    cert: str = None
    cert_cn = None
    cert_dn = None

    def parser(self, connInfo):
        for info in connInfo:
            key = info[0]
            if key == b'socktype':
                socktype = SockType()
                self.socket_type = socktype.get_socktype(info[1])
            elif key == b'peername':
                ip_tuple, port = info[1]
                self.peername_ip = '.'.join(map(str, ip_tuple))
                self.peername_port = port
            elif key == b'sockname':
                self.socket_ip = '.'.join(map(str, ip_tuple))
                self.socket_name = port
            elif key == b'peercert':
                cert_info = info[1]
                if cert_info == b'nossl':
                    self.cert = 'nossl'
                else:
                    self.cert_cn = cert_info[0]
                    self.cert_dn = cert_info[0]
            else:
                return "error"

    def __str__(self):
        s = f"EmqxConnectionInfo{{\n socketType='{self.socket_type}'\n socketIP='{self.socket_ip}'\n socketPort='{self.socket_name}' \n peerNameIp='{self.peername_ip}' \n peerNamePort='{self.peername_port}' \n cert='{self.cert}' \n cert_cn='{self.cert_cn}' \n cert_dn='{self.cert_dn}'\n}}"
        return s
