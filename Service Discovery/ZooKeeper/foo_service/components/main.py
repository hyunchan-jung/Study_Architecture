import os
import random

import requests
from kazoo.client import KazooClient

zk = KazooClient(hosts='192.168.0.12:2181')
zk.start()


def call():
    path = '/foo-service'
    services = zk.get_children(path)

    selected_service = random.choice(services)
    service_data, _ = zk.get(path + '/' + selected_service)

    decoded_data = service_data.decode('utf-8')
    service_info = eval(decoded_data)

    return requests.get(f'http://{service_info["host"]}:{service_info["port"]}').json()


def some_business_logic():
    if os.environ.get('ROLE') == 'caller':
        return call()
    else:
        host = os.environ.get('HOSTNAME')
        return {
            'host': host
        }


def startup():
    if os.environ.get('ROLE') == 'callee':
        path = '/foo-service'
        zk.ensure_path(path)
        value = str({
            'host': os.environ.get('HOST'),
            'port': 8000
        }).encode('utf-8')
        zk.create(path=path + '/server', value=value, ephemeral=True, sequence=True)


def shutdown():
    zk.stop()
