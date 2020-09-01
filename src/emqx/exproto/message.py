from erlport import Atom
from .until import to_binary


class Message:
    idd: str
    qos: str
    from_: str
    topic: str
    payload: str
    timestamp: int

    def __init__(self, idd: str = '', qos: int = 0, from_: str = '', topic: str = '',
                 payload: str = '', timestamp: int = 0):
        self.idd = idd
        self.qos = qos
        self.from_ = from_
        self.topic = topic
        self.payload = payload
        self.timestamp = timestamp

    @staticmethod
    def parse(msg_obj) -> list:
        message_list = []
        for msg in msg_obj:
            message_list.append(Message.parse_one(msg))
        return message_list

    @staticmethod
    def parse_one(msg_tuple: tuple) -> 'Message':
        message = Message()
        for msg_obj in msg_tuple:
            key = bytes.decode(Atom(msg_obj[0]))
            value = msg_obj[1]
            if key == 'id':
                message.idd = bytes.decode(value)
            elif key == 'qos':
                message.qos = int(value)
            elif key == 'from':
                message.from_ = bytes.decode(value)
            elif key == 'topic':
                message.topic = bytes.decode(value)
            elif key == 'payload':
                message.payload = bytes.decode(value)
            elif key == 'timestamp':
                message.timestamp = int(value)
            else:
                continue
        return message

    @staticmethod
    def to_erlang_data_type(msg):
        tuple_list = [
            (Atom(b'id'), to_binary(msg.id)),
            (Atom(b'qos'), to_binary(msg.qos)),
            (Atom(b'from'), to_binary(msg.from_)),
            (Atom(b'topic'), to_binary(msg.topic)),
            (Atom(b'payload'), to_binary(msg.payload)),
        ]
        return tuple_list

    def __str__(self):
        string = f"EmqxDeliverMessage{{\n " \
            f"id={self.idd},\n " \
            f"qos={self.qos},\n " \
            f"from={self.from_},\n " \
            f"topic={self.topic},\n " \
            f"payload={self.payload},\n " \
            f"timestamp={self.timestamp}\n" \
            f"}}"
        return string