from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import SocketServer
import time

HOST, PORT = 'localhost', 8000

class AsyncXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer):
    pass

def delay(s):
    time.sleep(s)

def add(x, y):
    delay(3)
    return x + y

def subtract(x, y):
    delay(3)
    return x - y

def multiply(x, y):
    delay(3)
    return x * y

def divide(x, y):
    delay(3)
    return x / y

if __name__ == '__main__':
#    server = SimpleXMLRPCServer((HOST, PORT))  # single thread
    server = AsyncXMLRPCServer((HOST, PORT), SimpleXMLRPCRequestHandler)  # multithreading

    server.register_multicall_functions()
    server.register_function(add, 'remote_add')
    server.register_function(subtract, 'remote_subtract')
    server.register_function(multiply, 'remote_multiply')
    server.register_function(divide, 'remote_divide')

    print 'Listening on port %s ...' % PORT
    server.serve_forever()
