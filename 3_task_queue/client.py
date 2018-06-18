from kombu import Connection
from queues import task_exchange, task_queues
from tasks import say

with Connection("amqp://") as conn:
    producer = conn.Producer()
    producer.publish({
        "func": say,
        "args": ("lijie",)
    },routing_key="hipri", declare=task_queues, exchange=task_exchange, serializer="pickle")
    producer.close()





