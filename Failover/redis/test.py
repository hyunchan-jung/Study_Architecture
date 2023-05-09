import time

import redis

sentinel_conn = redis.Sentinel([
    ('192.168.57.101', 26379),
    ('192.168.57.102', 26379),
    ('192.168.57.103', 26379)
])


def test():
    try:
        master = sentinel_conn.discover_master('mymaster')
        slaves = sentinel_conn.discover_slaves('mymaster')
        print('master:', master)
        print('slaves:', slaves)

        print('foo:', sentinel_conn.master_for('mymaster').get('foo'))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    redis_conn = redis.Redis('192.168.57.101', 6379)
    redis_conn.set('foo', 'bar')

    for _ in range(120):
        test()
        time.sleep(1)
