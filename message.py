from erlport import Atom

class Message:
    def __init__(self, idd: str=None, qos: int=None, from_: str=None, topic: str=None, payload: bytes=None, timestamp: int=None):
        self.idd = idd
        self.qos = qos
        self.from_ = from_
        self.topic = topic
        self.payload = payload
        self.timestamp = timestamp

    @staticmethod
    def parse(msg_obj):
        message_list = []
        for msg in msg_obj:
            ...

    @staticmethod 
    def parse_one(msg_list: list):
        message = Message()
        for msg_obj in msg_list:
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
        

