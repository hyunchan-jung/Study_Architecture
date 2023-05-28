import random

import redis


class RangeShardManager:
    shards = {
        "0": redis.StrictRedis(host="localhost", port=6380),
        "1": redis.StrictRedis(host="localhost", port=6381),
        "2": redis.StrictRedis(host="localhost", port=6382),
    }

    def get_conn_by_id(self, user_id: int):
        if user_id <= 10000:
            return self.shards["0"]
        elif user_id <= 20000:
            return self.shards["1"]
        elif user_id <= 30000:
            return self.shards["2"]
        else:
            return None


if __name__ == "__main__":
    rsm = RangeShardManager()
    for _ in range(100):
        user_id = random.randint(0, 30000)
        conn = rsm.get_conn_by_id(user_id)
        print(user_id, conn.connection_pool)
