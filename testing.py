import json

l = {'name': 'qcli_volume -c lv_type raidLevel diskID Threshold encrypt SSDCache Alias', 'request': {'method': 'GET', 'header': [], 'body': {}, 'url': {'raw': '{{PREFIX}}/cgi-bin/disk/disk_manage.cgi?&func=model_get_limitation&sid=atrnsrfw1qmi3tdelqs103vr9stirjjs&count=13471.875223', 'host': ['{{PREFIX}}'], 'path': ['cgi-bin', 'disk', 'disk_manage.cgi'], 'query': [{'key': 'func', 'value': 'model_get_limitation', 'equals': True}, {'key': 'sid', 'value': 'atrnsrfw1qmi3tdelqs103vr9stirjjs', 'equals': True}, {'key': 'count', 'value': '13471.875223', 'equals': True}, {'key': '', 'value': ''}]}, 'description': ''}, 'response': []}
a = json.dumps(l, sort_keys=True, indent=4, separators=(',', ': '))
# print(a)

new_query = {'key': 'ww', 'value': 'ww', 'equals': True}
l['request']['url']['query'].append(new_query)


test = {
	"info": {
		"name": "TESTTE copy",
		"_postman_id": "6e56bfe2-e541-5fbf-c5d2-09a67126ac07",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
	]
}

encodedjson = json.dumps(test)
print(repr(test))
print(encodedjson)
