import socket


def some_business_logic():
    host = socket.gethostname()
    return {
        'ip': socket.gethostbyname(host),
    }
