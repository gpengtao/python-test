from ws4py.websocket import WebSocket
from ws4py.server.geventserver import WSGIServer
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import time, random


class EchoWebSocket(WebSocket):
    def received_message(self, message):
        """
        Automatically sends back the provided ``message`` to
        its originating endpoint.
        """
        print message.__dict__
        while True:
            try:
                value = random.uniform(50, 900000)
                s = "x" * int(value)
                self.send(s, message.is_binary)
                time.sleep(0.01)
                print "send " + str(value)
            except BaseException:
                print "error"


server = WSGIServer(('0.0.0.0', 9700), WebSocketWSGIApplication(handler_cls=EchoWebSocket))
server.serve_forever()
