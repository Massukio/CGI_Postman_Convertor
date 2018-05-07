import re

s = '/cgi-bin/disk/disk_manage.cgi?&func=model_get_limitation&sid=atrnsrfw1qmi3tdelqs103vr9stirjjs&count=13471.875223'


def url_divider(text):
    # replace '/' and '?' with blank space
    tmp_arr = text.replace('/',' ').replace('?',' ').split(' ')

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

a, b = url_divider(s)
print(url_divider(s))


def query_divider(text):
    key = text.split("=")[0]
    value = text.split("=")[1]

    query = {'key': text.split("=")[0], 'value': text.split("=")[1]}