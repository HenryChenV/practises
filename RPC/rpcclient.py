import xmlrpclib
import datetime

HOST, PORT = 'localhost', 8000

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy('http://%s:%d/' % (HOST, PORT))

    multicall = xmlrpclib.MultiCall(proxy)
    multicall.remote_add(7, 3)
    multicall.remote_subtract(7, 3)
    multicall.remote_multiply(7, 3)
    multicall.remote_divide(7, 3)
#    raw_input('Pressing Any Key to Continue ...')

    time_start = datetime.datetime.now()
    resp = multicall()
    time_end = datetime.datetime.now()
    time_delta = time_end - time_start
    print resp.results
    print time_delta
