# get ip

import socket
#import socket
#import fcntl
#import struct
#windows:
def get_host_ip():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr

#linux:
def linux_get_host_ip():
    import socket
    import fcntl
    import struct



#def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,
#        struct.pack('256s', ifname[:15])
#        )[20:24])


#>>> get_ip_address('lo')
#'127.0.0.1'

#>>> get_ip_address('eth0')
#'38.113.228.130'