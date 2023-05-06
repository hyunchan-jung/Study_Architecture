import os
import random

import requests
from kazoo.client import KazooClient

HOST = os.getenv('HOST')
HOSTNAME = os.getenv('HOSTNAME')
ROLE = os.getenv('ROLE')  # 'caller' or 'callee'

SERVICE_NAME = 'foo-service' if HOSTNAME == 'node-02' else 'bar-service'

zk = KazooClient(hosts='192.168.0.12:2181')
zk.start()


def call(service_name: str):
    path = '/' + service_name
    services = zk.get_children(path)

    selected_service = random.choice(services)
    service_data, _ = zk.get(path + '/' + selected_service)

    decoded_data = service_data.decode('utf-8')
    service_info = eval(decoded_data)

    return requests.get(f'http://{service_info["host"]}:{service_info["port"]}').json()


def some_business_logic():
    if ROLE == 'caller':  # node-01
        return str(call('foo-service')) + str(call('bar-service'))
    else:
        return {
            'host': HOST,
            'host_name': HOSTNAME,
            'service_name': SERVICE_NAME,
        }


def startup():
    if ROLE == 'callee':  # node-02 and node-03
        path = '/' + SERVICE_NAME
        zk.ensure_path(path)
        value = str({
            'host': HOST,
            'port': 8000
        }).encode('utf-8')
        zk.create(path=path + '/server', value=value, ephemeral=True, sequence=True)


def shutdown():
    zk.stop()
