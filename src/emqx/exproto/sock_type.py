class ConstantsMeta(type):
    def __setattr__(self, key, value):
        raise AttributeError(f"you can't set this attribute: {key} = {value}")


class BaseConstant(metaclass=ConstantsMeta):
    ...


class SockType(BaseConstant):
    TCP = 'tcp'
    TLS = 'tls'
    UDP = 'udp'
    DTLS = 'dtls'

    def get_socktype(self, atom):
        sock_type = bytes.decode(atom)
        if sock_type == 'tcp':
            return self.TCP
        elif sock_type == 'tls':
            return self.TLS
        elif sock_type == 'udp':
            return self.UDP
        elif sock_type == 'dtls':
            return self.DTLS
        else:
            return None
