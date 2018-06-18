from kombu import Connection, Exchange, Queue

rmq_url = "amqp://guest:guest@localhost//"

media_exchange = Exchange("meida", type="direct")
video_queue = Queue("video", exchange=media_exchange, routing_key="video")

with Connection(rmq_url) as conn:
    producer = conn.Producer(serializer="json")
    producer.publish({
        "name": "xxx.avi",
        "size": "165421"
    }, exchange=media_exchange, routing_key="video")
