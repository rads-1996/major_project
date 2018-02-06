import csv
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer=KafkaProducer(bootstrap_servers=['broker:9092'])
topic="kddcup"

data=csv.reader(open('kddcup.data_10_percent_corrected.txt'),delimiter=',')
fields=data.next()
print fields
for row in data:
        item=dict(zip(fields,row))
        producer.send(topic,item)
