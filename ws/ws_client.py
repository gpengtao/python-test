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

ws = EchoClient('ws://192.168.1.50:9000/video?url=rtsp%3A%2F%2F192.168.1.10%2Fuser%3Dadmin%26password%3D%26channel%3D1%26stream%3D0.sdp', protocols=['http-only', 'chat'])
ws.connect()
ws.run_forever()
