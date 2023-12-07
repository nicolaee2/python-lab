import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

queue_name = 'webpages_queue'
channel.queue_declare(queue=queue_name)

tasks = [
    {"link": "http://example.com", "locatieDisk": "/path/to/save"},
]

for task in tasks:
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=json.dumps(task)
                          )

print(" [x] Sarcini trimise")
connection.close()
