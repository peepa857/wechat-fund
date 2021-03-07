import requests
import json
import re

# *fund codes array As target data*
fund_codes = [
    "161725", "320007", "260108", "001938", "003096", "006408", "000596"
]

# message for send to chat
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
        message += ("基金: <u>{}</u>，估算涨幅率: **{}%**\n".format(
            data['name'], data['gszzl']))

# post URL by WxPusher
wxPusher_url = "http://wxpusher.zjiecode.com/api/send/message"
# post body
wxPusher_data = {
    "appToken": "",  # *set your WxPusher APP Token*
    # "summary": "今日基金实时涨跌情况提醒",
    "content": message,
    "contentType": 3,  # values:「1:text,2:html,3:markdown」
    "topicIds": [1650],
    # "uids": [""], # *target wechat user id*
    # "url": "https://financeprod.alipay.com/account/finance/index.htm"
}
# send request
res = requests.post(url=wxPusher_url,
                    data=json.dumps(wxPusher_data),
                    headers=headers)
print(res.text)
