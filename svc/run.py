import time

from nameko.rpc import rpc
from runner import run


class ServiceRpc:
    name = "service_rpc"

    @rpc
    def task_1(self, name):
        print("task task_1 running ...")
        start_time = time.time()
        rate = 0
        max_range = 10000000
        for item in range(1, max_range):
            if round((item / max_range * 100), 0) == rate:
                # print(f" - rpc ", rate, "%")
                rate += 10

        # print(f"rpc excute time ", time.time() - start_time)

        print("task get_primes done")
        return f"rpc excute time {time.time() - start_time}"

    @rpc
    def get_primes(self, index):
        print("task get_primes running ...")
        prime = []

        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

        for i in range(1, index):
            if is_prime(i):
                prime.append(i)
        print("task get_primes done")
        return prime


CONFIG = {
    "AMQP_URI": "pyamqp://guest:guest@localhost",
}


if __name__ == "__main__":
    run([ServiceRpc], CONFIG)
