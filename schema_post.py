import requests

key_location = 'key.avsc'
value_location = "value.avsc"

key_fp = open(key_location)
value_fp = open(value_location)

schema_base_url = 'http://schema_registry:8081/'
print(schema_base_url)

key_resp = requests.post(schema_base_url+'subjects/{}-key/versions'.format(topic),
			 	json={'schema': key_fp.read() })

print(key_resp.json())

value_resp = requests.post(schema_base_url+'subjects/{}-value/versions'.format(topic),
				json={'schema': value_fp.read() })
print(value_resp.json())

key_fp.close()
value_fp.close()
