from kombu import Connection
from datetime import datetime

with Connection("amqp://") as conn:
    simple_queue = conn.SimpleQueue("video")
    msg = "hello world, sent at {0}".format(datetime.now())
    simple_queue.put(msg)
    print(msg)
    simple_queue.close()
