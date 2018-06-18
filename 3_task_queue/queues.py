from kombu import Queue, Exchange

task_exchange = Exchange("tasks", type="direct")
task_queues = [
    Queue("hipri", exchange=task_exchange, routing_key="hipri"),
    Queue("mdpri", exchange=task_exchange, routing_key="mdpri"),
    Queue("lwpri", exchange=task_exchange, routing_key="lwpri")
]
