# emqx-exproto-python-sdk

The Python SDK for emqx-exproto

### Installation

You can clone the git repository:
> git clone https://github.com/emqx/emqx-exproto-python-sdk.git
> cd emqx-exproto-python-sdk
> python3 setup.py install

### Interface

#### Callbacks

**Connection Layer callbacks**(The Connection object represents a TCP/UDP Socket entity):

```python
// This function will be scheduled after a TCP connection established to EMQ X
//  or receive a new UDP socket.
on_connect(connection: Connection, connection_info: ConnectionInfo)

// This callback will be scheduled when a connection received bytes from TCP/UDP socket.
on_received(connection: Connection, data: bytes, state: any)

// This function will be scheduled after a connection terminated.
//
// It indicates that the EMQ X process that maintains the TCP/UDP socket
// has been closed. E.g: a TCP connection is closed, or a UDP socket has
// exceeded maintenance hours.
on_terminated(connection: Connection, reason: str, state: any)
```

**Pub/Sub Layer callbacks:**

```python
// This function will be scheduled when a connection received a Message from EMQ X
//
// When a connection is subscribed to a topic and a message arrives on that topic,
// EMQ X will deliver the message to that connection. At that time, this function
// is triggered.
on_deliver(connection: Connection, message_list: list)
```

#### APIs

Similarly, AbstractExprotoHandler also provides a set of APIs to facilitate the use of the emqx-exproto APIs.

**Connection Layer APIs:**

```python
// Send a stream of bytes to the connection. These bytes are delivered directly
// to the associated TCP/UDP socket.
send(connection: Connection, data: bytes)

// Terminate the connection process and TCP/UDP socket.
terminate(connection: Connection)
```

**Pub/Sub Layer APIs:**

```python
// Register the connection as a Client of EMQ X. This `clientInfo` contains the
// necessary field information to be an EMQ X client.
//
// This method should normally be invoked after confirming that a connection is
// allowed to access the EMQ X system. For example: after the connection packet
// has been parsed and authenticated successfully.
register(connection: Connection, client_info: ClientInfo)

// The connection Publish a Message to EMQ X
publish(connection: Connection, message: Message)

// The connection Subscribe a Topic to EMQ X
subscribe(connection: Connection, topic: str, qos: int)
```

### Example

```python
from emqx.exproto.abstract_handler import AbstractExProtoHandler
from emqx.exproto.connection import Connection, ConnectionInfo


class SdkDemo(AbstractExProtoHandler):
    def on_connect(self, connection: Connection, connection_info: ConnectionInfo):
        print(connection)
        print(connection_info)

    def on_received(self, connection: Connection, data: bytes, state: any):
        print(connection)
        print(bytes.decode(data))

    def on_terminated(self, connection: Connection, reason: str, state: any):
        print(connection)
        print(reason)

    def on_deliver(self, connection: Connection, message_list: list):
        print(connection)
        for message in message_list:
            print(message)
```


### License

Apache License v2

### Author

- [Adek06](https://github.com/Adek06)