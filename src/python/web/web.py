import SimpleHTTPServer
import SocketServer


class CustomHttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler, object):

    def do_GET(self):
        super(CustomHttpHandler, self).do_GET()


if __name__ == "__main__":
    serverPort = 8000
    webServer = SocketServer.TCPServer(("", serverPort), CustomHttpHandler)
    print("Server started at port %s" % serverPort)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
