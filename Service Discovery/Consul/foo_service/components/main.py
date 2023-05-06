import os

import requests
from consul import Consul, Check

HOST = os.getenv('HOST')
HOSTNAME = os.getenv('HOSTNAME')
ROLE = os.getenv('ROLE')  # 'caller' or 'callee'

SERVICE_NAME = 'foo-service' if HOSTNAME == 'node-02' else 'bar-service'
SERVICE_ID = f"{SERVICE_NAME}-instance-01"

consul = Consul(host='192.168.0.12', port=8500)


def call(service_name: str):
    service_entry = consul.catalog.service(service_name)[1][0]
    url = f"http://{service_entry['ServiceAddress']}:{service_entry['ServicePort']}"

    return requests.get(url).json()


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
        check_url = f"http://{HOST}:8000/health"

        consul.agent.service.register(
            name=SERVICE_NAME,
            service_id=SERVICE_ID,
            address=HOST,
            port=8000,
            check=Check.http(url=check_url, interval='10s'),
        )


def shutdown():
    if ROLE == 'callee':  # node-02 and node-03
        consul.agent.service.deregister(
            service_id=SERVICE_ID,
        )
