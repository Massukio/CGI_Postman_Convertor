import json
import os
import copy


class CGI_Postman(object):

    def __init__(self):
        self.postman_json_format = {'info': {'name': 'TESTTE copy', '_postman_id': '6e56bfe2-e541-5fbf-c5d2-09a67126ac07', 'schema': 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'}, 'item': []}
        self.request_json_format = {'name': 'request_name', 'request': {'method': 'GET', 'header': [], 'body': {}, 'url': {'raw': 'request_url', 'host': ['{{PREFIX}}'], 'path': [], 'query': []}, 'description': ''}, 'response': []}

    def read_file(self, file_path):
        with open(file_path) as f:
            content = f.readlines()
            # remove whitespace characters like `\n` at the end of each line
            self.content = [x.strip() for x in content]
        return self.content

    def convertor(self, arr):
        items = []
        tmp_json = copy.deepcopy(self.request_json_format)

        for arr_node in arr:
            if 'qcli_' in arr_node:
                tmp_json['name'] = arr_node
            elif '/cgi-bin' in arr_node:
                tmp_json['request']['url']['raw'] = arr_node
                path_arr, query_arr = self.url_divider(arr_node)

                for path_node in path_arr:
                    tmp_json['request']['url']['path'].append(path_node)

                for query_node in query_arr:
                    tmp_json['request']['url']['query'].append({'key': query_node.split("=")[0], 'value': query_node.split("=")[1]})

                if self.item_complete_judge(tmp_json):
                    items.append(tmp_json)
                    tmp_json = copy.deepcopy(self.request_json_format)
            else:
                print("Invalid input: " + arr_node)

        return items

    def item_complete_judge(self, tmp_json):
        if ('qcli_' in tmp_json['name']) and ('cgi-bin' in tmp_json['request']['url']['path']):
            return True
        else:
            return False

    def url_divider(self, text):
        # replace '/' and '?' with blank space
        tmp_arr = text.replace('/', ' ').replace('?', ' ').split(' ')

        # remove blank space from the first node
        del tmp_arr[0]

        # save path and query into separated arrays
        path_ret = []
        query_ret = []

        for i in tmp_arr:
            if '&' not in i:
                path_ret.append(i)
            else:
                query_ret = i.split('&')
                del query_ret[0]

        return path_ret, query_ret

    def package(self, arr):

        for i in arr:
            self.postman_json_format['item'].append(i)

        return self.postman_json_format


test = CGI_Postman()
items = test.convertor(test.read_file('c:\\test.log'))
collection = json.dumps(test.package(items), sort_keys=False, indent=4, separators=(',', ': '))
print(collection)
