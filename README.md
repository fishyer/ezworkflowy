# EZWorkflowy

EZWorkflowy是一个基于Workflowy的TelegramBot,方便通过Telegram机器人快速添加笔记到Workflowy。

## 使用效果

手机上通过TG来快速收集

![](https://yupic.oss-cn-shanghai.aliyuncs.com/telegram-cloud-photo-size-5-6258063183780625333-y.jpg?x-oss-process=image/resize,w_200,limit_0)

电脑上通过WF来批量整理

![](https://yupic.oss-cn-shanghai.aliyuncs.com/202406011616263.png)

## 使用说明

1-配置.env文件

```
TOKEN="7298149992:AAEZhKfwiyGjsr5hKGuIid2f-2XXXXXXXXXX"
SESSION_ID="bza32axq7bbzt9w5h1k6b163XXXXXXXX"
```

2-运行docker

```
docker-compose up -d --build
```

## 如果获取2个配置参数

TOKEN: 通过Telegram BotFather获取，[Telegram BotFather](https://t.me/botfather)，自己新建一个bot，然后获取token。

SESSION_ID: 登录Workflowy，打开浏览器的开发者工具，通过Application->Storage->Cookie，找到https://workflowy.com 的cookie，再找到名为"SESSIONID"的键值对，复制其值。