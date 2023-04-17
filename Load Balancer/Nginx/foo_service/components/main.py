import os


def some_business_logic():
    host = os.environ.get('HOSTNAME')
    return {
        'host': host
    }
