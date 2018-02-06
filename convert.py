import csv
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

def create_kddcup_value_record(item):
    return {
        "duration": int(item["duration"]),
        "protocol_type": item["protocol_type"],
        "service": item["service"],
        "flag": item["flag"],
        "src_bytes": int(item["src_bytes"]),
        "dst_bytes": int(item["dst_bytes"]),
        "land": int(item["land"]),
        "wrong_fragment": int(item["wrong_fragment"]),
        "urgent": int(item["urgent"]),
        "hot": int(item["hot"]),
        "num_failed_logins": int(item["num_failed_logins"]),
        "logged_in": int(item["logged_in"]),
        "num_compromised": int(item["num_compromised"]),
        "root_shell": int(item["root_shell"]),
        "su_attempted": int(item["su_attempted"]),
        "num_root": int(item["num_root"]),
        "num_file_creations": int(item["num_file_creations"]),
        "num_shells": int(item["num_shells"]),
        "num_access_files": int(item["num_access_files"]),
        "num_outbound_cmds": int(item["num_outbound_cmds"]),
        "is_host_login": int(item["is_host_login"]),
        "is_guest_login": int(item["is_guest_login"]),
        "count": int(item["count"]),
        "srv_count": int(item["srv_count"]),
        "serror_rate": float(item["serror_rate"]),
        "srv_serror_rate": float(item["srv_serror_rate"]),
        "rerror_rate": float(item["rerror_rate"]),
        "srv_rerror_rate": float(item["srv_rerror_rate"]),
        "same_srv_rate": float(item["same_srv_rate"]),
        "diff_srv_rate": float(item["diff_srv_rate"]),
        "srv_diff_host_rate": float(item["srv_diff_host_rate"]),
        "dst_host_count": int(item["dst_host_count"]),
        "dst_host_srv_count": int(item["dst_host_srv_count"]),
        "dst_host_same_srv_rate": float(item["dst_host_same_srv_rate"]),
        "dst_host_diff_srv_rate": float(item["dst_host_diff_srv_rate"]),
        "dst_host_same_src_port_rate": float(item["dst_host_same_src_port_rate"]),
        "dst_host_srv_diff_host_rate": float(item["dst_host_srv_diff_host_rate"]),
        "dst_host_serror_rate": float(item["dst_host_serror_rate"]),
        "dst_host_srv_serror_rate": float(item["dst_host_srv_serror_rate"]),
        "dst_host_rerror_rate": float(item["dst_host_rerror_rate"]),
        "dst_host_srv_rerror_rate": float(item["dst_host_srv_rerror_rate"]),
        "label": item["label"]
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
        print(value_rec)
        avroProducer.produce(topic=topic, value=value_rec, key="")
avroProducer.flush()
