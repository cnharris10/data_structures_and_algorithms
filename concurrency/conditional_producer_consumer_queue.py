import threading
from collections import deque


class ConditionalProducerConsumerQueue():
    name = "Concurrent Queue with Conditional Lock"

    @classmethod
    def demo(cls):
        qw = QueueWrapper(counter_limit=100)
        producers = []
        consumers = []
        producer_limit = 3
        consumer_limit = 3

        # Start all producer threads
        for _ in range(producer_limit):
            p = Producer(qw)
            pt = threading.Thread(target=p.run, daemon=True)
            producers.append(pt)
            pt.start()

        # Start all consumer threads
        for _ in range(consumer_limit):
            c = Consumer(qw)
            ct = threading.Thread(target=c.run, daemon=True)
            consumers.append(ct)
            ct.start()

        for p in producers:
            p.join()

        # No more items to add, let consumers drain
        qw.close()

        for c in consumers:
            c.join()

        print(f"{producer_limit} producers spawned.")
        print(f"{consumer_limit} consumers spawned.")


class QueueWrapper:

    def __init__(self, counter_limit = 100000):
        self.q = deque(maxlen=100)
        self.counter = 0
        self.closed = False
        self.condition = threading.Condition()
        self.counter_limit = counter_limit

    def add(self) -> bool:
        with self.condition:
            # Queue is full and not closed
            while(len(self.q) >= self.q.maxlen and not self.closed):
                self.condition.wait()

            # Whether to produce at all, kept separate from whether there is room
            if self.closed or self.counter >= self.counter_limit:
                return False

            # Append current, increment counter, wake up all
            self.q.append(self.counter)
            self.counter += 1
            self.condition.notify_all()
            return True

    def remove(self):
        with self.condition:
            # Queue is full and not closed
            while(len(self.q) <= 0 and not self.closed):
                self.condition.wait()

            # None, not False: 0 is a legitimate item and is falsy
            if len(self.q) <= 0:
                return None

            item = self.q.popleft()
            self.condition.notify_all()
            return item

    def close(self):
        with self.condition:
            # Flag that producers are done and wake up all threads
            self.closed = True
            self.condition.notify_all()

    def printq(self):
        with self.condition:
            # Print current state of q
            print(list(self.q))

class Producer:

    def __init__(self, qw):
        self.qw = qw

    def run(self):
        while self.qw.add():
            self.qw.printq()

class Consumer:

    def __init__(self, qw: QueueWrapper):
        self.qw = qw

    def run(self):
        while self.qw.remove() is not None:
            self.qw.printq()


if __name__ == "__main__":
    ConditionalProducerConsumerQueue.demo()
