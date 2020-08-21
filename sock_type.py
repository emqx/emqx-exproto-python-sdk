class SockType:
    TCP = 'tcp'
    TLS = 'tls'
    UDP = 'udp'
    DTLS = 'dtls'

    def get_socktype(self, atom):
        if atom == Atom(b'tcp'):
            return self.TCP
        elif atom == Atom(b'tls'):
            return self.TLS
        elif atom == Atom(b'udp'):
            return self.UDP
        elif atom == Atom(b'dtls'):
            return self.DTLS
        else:
            return None
    