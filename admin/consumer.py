# amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik
import pika

params = pika.URLParameters('amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')
 
def callback(ch, method, properties, body):
    print("received in admin app")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
