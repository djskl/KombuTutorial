from kombu import Connection, Queue, Consumer

def process_media(body, msg):
    print(body)
    msg.ack()

video_queue = Queue("video", exchange="", routing_key="video")

with Connection("amqp://") as conn:
    with conn.Consumer(queues=video_queue, callbacks=[process_media]) as consumer:
        conn.drain_events()

# conn = Connection("amqp://")
# consumer = Consumer(conn, queues=video_queue)
# consumer.register_callback(process_media)
# consumer.consume()
# conn.drain_events()

# with Connection("amqp://") as conn:
#     q = conn.SimpleQueue("video")
#     msg = q.get()
#     print(msg)
#     msg.ack()
#     q.close()