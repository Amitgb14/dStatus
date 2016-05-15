# -*- coding: utf-8 -*-

import SocketServer
import sys
import dscan
import config


class RunServer(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        reports = dscan.main()
        # send back data
        self.request.sendall(str(reports))


if __name__ == "__main__":
    HOST, PORT = config.CLIENT_IP, config.CLIENT_PORT

    # Create the server, binding to 0.0.0.0 on port 9999
    server = SocketServer.TCPServer((HOST, PORT), RunServer)
    print("Running server on port {}".format(PORT))

    try:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exit server...")
        sys.exit(0)
