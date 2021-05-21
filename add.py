import requests
import json
import os

response = json.loads(requests.get("https://chia.powerlayout.com/nodes?block_height=true&geoip=true").text)
for node in response['nodes']:
	chia_node = node['ip'] + ":" + node['port']
	os.system("chia show -a " + chia_node)
import requests
import json
import os

response = json.loads(requests.get("https://chia.powerlayout.com/nodes?block_height=true&geoip=true").text)
for node in response['nodes']:
	chia_node = node['ip'] + ":" + node['port']
	os.system("chia show -a " + chia_node)
