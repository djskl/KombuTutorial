from kombu import Connection

with Connection("amqp://") as conn:
    simple_queue = conn.SimpleQueue("video")
    msg = simple_queue.get()
    print(msg.payload)
    msg.ack()
    simple_queue.close()