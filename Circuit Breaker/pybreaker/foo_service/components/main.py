import time
import random

import pybreaker

cb = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=3)


@cb
def call():
    if random.choice([True, False]):
        raise Exception('error')

    return 'ok'


def some_business_logic():
    results = {}
    for n in range(20):
        n = str(n).zfill(2)

        try:
            results[n] = call()
        except pybreaker.CircuitBreakerError as e:
            results[n] = str(e)
        except Exception as e:
            results[n] = str(e)

        time.sleep(1)

    return results


def startup():
    pass


def shutdown():
    pass
