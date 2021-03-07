# wechat-fund

Real time view of funds earnings yield

## create WxPusher APP

[WxPusher 微信信息推送服务](https://wxpusher.zjiecode.com/admin/)

## environment and dependencies

- python 3.9.1

- pip 20.2.3

- `pip install requests`

## set params

- appToken: get the token after created a WxPusher APP(line: 41)

- topicIds: get topicId after created a topic of APP(line: 45)

## run command

- `py fund.py` send message to wechat

## screen shot

![image](https://github.com/peepa857/wechat-fund/blob/master/image/wx-message.png)

![image](https://github.com/peepa857/wechat-fund/blob/master/image/message-detail.png)

## my fund APP QRcode

![image](https://github.com/peepa857/wechat-fund/blob/master/image/qrcode.png)

## scheduled job

[cron の使い方（python スクリプト）](https://qiita.com/saira/items/76a5538a6b2556f6b339)
