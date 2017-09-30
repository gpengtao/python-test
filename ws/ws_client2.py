from ws4py.client.threadedclient import WebSocketClient
from ws4py.messaging import Message, PingControlMessage,\
    PongControlMessage


class EchoClient(WebSocketClient):
    def opened(self):
       for i in range(0, 200, 25):
          self.send("*" * i)
          self.send(PingControlMessage('fuck'))

    def closed(self, code, reason):
       print(("Closed down", code, reason))

    def received_message(self, m):
       print("=> %d %s" % (len(m), "on message"))

    def ponged(self, pong):
        print "pong:",pong.__dict__

ws = EchoClient('ws://127.0.0.1:9700/', protocols=['http-only', 'chat'])
ws.connect()
ws.run_forever()
