import os
import pika, json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
URL = open(os.path.join(__location__, '../secret-url.txt')).read()

params = pika.URLParameters(URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

# Publish in the main app rather than the admin app
def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)