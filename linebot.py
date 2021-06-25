import requests
import json
import re
import time

# fund codes array As target data
fund_codes = [
    "161725",
    "320007",
    "260108",
    "001938",
    "003096",
    "006408",
    "003834",
    "001838",
    "519674",
]

# line channel access token
access_token = 'WaQ79DcsAgvTF0deitRZsS0TkJZLTaDMKFBlUDdOGy6ArBQjMDBwQJHKdyo4PIudjQXRXgKwTomYn8sLNd5RIP1eOu9eLeHdFB9/Ej5P+xOBaG1u3/GDYBUjRM/coQg+Z0MRkDYoLj+y4cbSccrctgdB04t89/1O/w1cDnyilFU='

# message for send to line
message = ""

for code in fund_codes:
    # request URL from https://fund.eastmoney.com/
    fund_url = "http://fundgz.1234567.com.cn/js/%s.js" % code
    # http request header
    headers = {
        'content-type':
        'application/json',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    # send request
    r = requests.get(url=fund_url, headers=headers)
    # returned body
    content = r.text
    # regexp
    pattern = r'^jsonpgz\((.*)\)'
    # format response
    search = re.findall(pattern, content)
    # get fund data from array
    for i in search:
        data = json.loads(i)
        if float(data['gszzl']) > 0:
            message += ("{}: {}%⬆️\n".format(data['name'], data['gszzl']))
        elif float(data['gszzl']) < 0:
            message += ("{}: {}%⬇️\n".format(data['name'], data['gszzl']))
        else:
            message += ("{}: {}%\n".format(data['name'], data['gszzl']))

# line messaging api url
line_url = 'https://api.line.me/v2/bot/message/broadcast'
# line request header
line_headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# define message in json format
message_list = {'messages': [{'type': 'text', 'text': message[:-1]}]}

# encode to json
data = json.dumps(message_list)
response = requests.post(url=line_url, headers=line_headers, data=data)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(response)
