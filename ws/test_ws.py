from gevent import monkey; monkey.patch_all()
from ws4py.websocket import WebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication


class EchoWebSocket(WebSocket):
    def received_message(self, message):
        """
        Automatically sends back the provided ``message`` to
        its originating endpoint.
        """
        print message.__dict__
        self.send(message.data, message.is_binary)


server = WSGIServer(('0.0.0.0', 9700), WebSocketWSGIApplication(handler_cls=EchoWebSocket))
server.serve_forever()




from ws4py.client.threadedclient import WebSocketClient

class EchoClient(WebSocketClient):
    def opened(self):
       for i in range(0, 200, 25):
          self.send("*" * i)

    def closed(self, code, reason):
       print(("Closed down", code, reason))

    def received_message(self, m):
       print("=> %d %s" % (len(m), str(m)))

    def ponged(self, pong):
        print "pong:",str(pong)

try:
    ws = EchoClient('ws://10.101.4.175:9700/', protocols=['http-only', 'chat'])
    ws.connect()
except KeyboardInterrupt:
    ws.close()