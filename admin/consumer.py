# amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik
import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://buhobiik:siLIsKgTv9_gPdOyyhzhy6UllHXlJTWB@rattlesnake.rmq.cloudamqp.com/buhobiik')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')
 
def callback(ch, method, properties, body):
    print("received in admin app")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1 
    product.save()
    print("product likes increased.")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
