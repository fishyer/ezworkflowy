# EZWorkflowy

EZWorkflowy是一个基于Workflowy的TelegramBot,方便通过Telegram机器人快速添加笔记到Workflowy。


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


## 命令备忘

pkill -f "python -u /Users/yutianran/Documents/MyCode/ezworkflowy/main.py"

pipreqs ./

docker init

docker-compose up -d --build