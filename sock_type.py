from erlport import Atom

class SockType:
    TCP = 'tcp'
    TLS = 'tls'
    UDP = 'udp'
    DTLS = 'dtls'

    def get_socktype(self, atom):
        if atom == b'tcp':
            return self.TCP
        elif atom == b'tls':
            return self.TLS
        elif atom == b'udp':
            return self.UDP
        elif atom == b'dtls':
            return self.DTLS
        else:
            return None
    