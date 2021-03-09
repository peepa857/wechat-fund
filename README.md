# wechat-fund

Real time view of funds earnings yield

## environment

- python 3.9.1

- pip 20.2.3

## create WxPusher APP

[WxPusher 微信信息推送服务](https://wxpusher.zjiecode.com/admin/)

## set params

- appToken: get the token after created a WxPusher APP (line: 41)

- topicIds: get topicId after created a topic of APP (line: 45)

## install dependencies

- `pip install requests`

## run command

- `py fund.py` send message to wechat

## screen shot

![image](https://github.com/peepa857/wechat-fund/blob/master/image/wx-message.png)

![image](https://github.com/peepa857/wechat-fund/blob/master/image/message-detail.png)

## my fund APP QRcode

![image](https://github.com/peepa857/wechat-fund/blob/master/image/qrcode.png)

## scheduled job

macOS/Linux: [cron の使い方（python スクリプト）](https://qiita.com/saira/items/76a5538a6b2556f6b339)

1. create shell `start.sh`

```shell
#!/bin/bash
source /etc/profile
python3 {FULL PATH}/wechat-fund/fund.py
```

2. crontab

- edit crontab

  `crontab -e`

- paste, replace path and save (run at working day 14:45)

  `45 14 * * 1-5 {FULL PATH}/start.sh >> {FULL PATH}/Desktop/crontab_log.txt`

- confirm results

  `crontab -l`
