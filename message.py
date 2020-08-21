from erlport import Atom
from until import to_binary
import itertools

class Message:
    idd: str 
    qos: str
    from_: str
    topic: str
    payload: str
    timestamp: int

    def __init__(self, idd: str=None, qos: int=None, from_: str=None, topic: str=None, payload: str=None, timestamp: int=None):
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
    def parse_one(msg_tuple: tuple) -> Message:
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
        
    def toErlangDataType(self, msg: Message):
        atom_list = [Atom(b'id'), Atom(b'qos'), Atom(b'from'), Atom(b'topic'), Atom(b'payload'), Atom(b'tamptime')]
        msg_list = list(map(to_binary, [msg.idd, msg.qos, msg.from_, msg.topic, msg.payload, msg.timestamp]))

        tuple_list = list(itertools.product(atom_list, msg_list))
        return tuple_list

    def __str__(self):
        s = f"EmqxDeliverMessage{{\n id={self.idd},\n qos={self.qos},\n from={self.from_},\n topic={self.topic},\n payload={self.payload},\n timestamp={self.timestamp}\n}}"
        return s
