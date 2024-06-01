from telegram import Update, ForceReply
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import requests
from ezlogger import print, logger
from wfapi import *
from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

# 从环境变量中读取TOKEN
TOKEN = os.getenv("TOKEN")
SESSION_ID = os.getenv("SESSION_ID")
print(f"TOKEN: {TOKEN}")
print(f"SESSION_ID: {SESSION_ID}")

# 定义全局变量
POST_URL = "https://httpbin.org/post"  # 替换为你打算POST的URL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """发送一条消息来提示用户启动了BOT"""
    user = update.effective_user
    print(f"User {user.username} started the bot")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hi {user.mention_markdown_v2()}! Send me a message and I will POST it!",
        parse_mode="MarkdownV2",
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """接收用户的消息，并发送一个POST请求"""
    received_message = update.message.text
    print(f"Received message: {received_message}")

    try:
        # 添加消息到Workflowy
        message_node = add(telegram_node, received_message)
        print(f"Message added to Workflowy: {message_node.name}")
        # data = {"message": received_message}
        # response = requests.post(POST_URL, json=data)
        # if response.status_code == 200:
        #     print("Message sent via POST successfully!")
        #     print(response.json())
        #     await update.message.reply_text("Message sent via POST successfully!")
        # else:
        #     logger.warning("Failed to send message via POST!")
        #     await update.message.reply_text("Failed to send message via POST!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        await update.message.reply_text(f"An error occurred: {e}")


def get_wf():
    wf = Workflowy(sessionid=SESSION_ID)
    return wf


def search(node: Node, title: str) -> Node:
    for child in node:
        print(child.name)
        if child.name == title:
            return child
    return None


def add(node: Node, title: str, content: str = None):
    sub_node = node.create()
    sub_node.edit(title)
    if content:
        sub_node.description = content
    return sub_node


# 获取Telegram-Inbox节点
def get_inbox(node: Node):
    inbox_name = "Telegram-Inbox"
    search_result = search(node, inbox_name)
    if search_result:
        print(f"Inbox found: {inbox_name}")
        return search_result
    else:
        print(f"Inbox created: {inbox_name}")
        return add(node, inbox_name)


def init_tg():
    """启动bot"""
    # 使用Application.builder创建Application实例
    application = Application.builder().token(TOKEN).build()
    print("Bot started successfully!")

    # 注册Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 开始Polling
    print("Bot is now polling...")
    application.run_polling()


def init_wf():
    global telegram_node
    print("Start to connect to Workflowy...")
    wf = get_wf()
    print("Connected to Workflowy.")
    telegram_node = get_inbox(wf.root)
    print(f"Telegram node: {telegram_node.name}")


def main() -> None:
    init_wf()
    init_tg()


if __name__ == "__main__":
    main()
