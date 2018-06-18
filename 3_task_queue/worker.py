from kombu import Connection
from kombu.mixins import ConsumerMixin
from kombu.utils import reprcall
from queues import task_queues

class Worker(ConsumerMixin):

    def __init__(self, conn):
        self.connection = conn

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=task_queues, callbacks=[self.process_task], accept=["pickle", "json"])]

    def process_task(self, body, msg):
        func = body["func"]
        args = body.get("args") or []
        kwargs = body.get("kwargs") or {}

        print("Got task: %s"%reprcall(func.__name__, args, kwargs))

        try:
            func(*args, **kwargs)
        except Exception as e:
            print("task raised exception:", e)

        msg.ack()

if __name__ == "__main__":

    with Connection("amqp://") as conn:
        worker = Worker(conn)
        try:
            worker.run()
        except KeyboardInterrupt:
            print("bye bye")



