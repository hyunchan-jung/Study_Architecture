import sys


def main(hostname):
    node01_ip = '192.168.57.101'

    # redis.conf
    with open('/Study_Architecture/Failover/redis/redis.conf', 'r') as f:
        lines = f.readlines()

    if hostname != 'node-01':
        lines += [
            f'replicaof {node01_ip} 6379\n',
        ]

    with open('/tmp/redis.conf', 'w') as f:
        f.writelines(lines)

    # sentinel.conf
    with open('/Study_Architecture/Failover/redis/sentinel.conf', 'r') as f:
        lines = f.readlines()

    lines += [
        f'sentinel monitor mymaster {node01_ip} 6379 2\n',
        'sentinel down-after-milliseconds mymaster 10000\n',
        'sentinel failover-timeout mymaster 60000\n',
        'sentinel parallel-syncs mymaster 1\n'
    ]

    with open('/tmp/sentinel.conf', 'w') as f:
        f.writelines(lines)


if __name__ == "__main__":
    argv = sys.argv
    main(*argv[1:])
