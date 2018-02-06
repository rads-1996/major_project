import csv
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

def create_kddcup_value_record(item):
    return {
        "duration": int(item["duration"]),
        "protocol_type": item["protocol_type"],
        "service": item["service"],
        "flag": item["flag"]
        # so on with other fields
    }

topic = "kddcup"
value_schema = avro.load('key.avsc')
key_schema = avro.load('value.avsc')

avroProducer = AvroProducer(
        {'bootstrap.servers': 'broker:9092', 'schema.registry.url': 'http://schema_registry:8081'},
        default_key_schema=key_schema,
        default_value_schema=value_schema
)

data=csv.reader(open('kddcup.data_10_percent_corrected.txt'),delimiter=',')
fields=data.__next__()
print(fields)
for row in data:
        item = dict(zip(fields,row))
        print(item)
        value_rec = create_kddcup_value_record(item)
        avroProducer.produce(topic=topic, value=value_rec, key="")
avroProducer.flush()
