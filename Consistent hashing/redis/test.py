import redis
import zlib

nodes = [
    {'host': '127.0.0.1', 'port': 6380},
    {'host': '127.0.0.1', 'port': 6381},
    {'host': '127.0.0.1', 'port': 6382},
]


def get_node(key):
    hash_value = zlib.crc32(key.encode()) & 0xffffffff
    node_index = hash_value % len(nodes)
    print('key:', key, 'hash:', hash_value, 'node:', node_index)
    return nodes[node_index]


def set_data(key, value):
    node = get_node(key)
    r = redis.Redis(host=node['host'], port=node['port'])
    r.set(key, value)


def get_data(key):
    node = get_node(key)
    r = redis.Redis(host=node['host'], port=node['port'])
    return r.get(key)


if __name__ == '__main__':
    import random
    from string import ascii_letters

    for _ in range(10000):
        key = ''.join(random.choice(ascii_letters) for _ in range(10))
        set_data(key, 'value')
        print(get_data(key))

    # Each node key counts
    for node in nodes:
        r = redis.Redis(host=node['host'], port=node['port'])
        print(node, len(r.keys()))
