# amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik
import pika, json

params = pika.URLParameters('amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
