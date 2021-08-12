import os
import pika

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
URL = open(os.path.join(__location__, '../secret-url.txt')).read()

params = pika.URLParameters(URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')