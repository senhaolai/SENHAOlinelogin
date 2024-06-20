# utils.py

from linebot import LineBotApi
from linebot.models import TextSendMessage
from django.conf import settings

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def send_line_message(user_id, message):
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text=message))
        print(f"訊息已發送給 {user_id}")
    except Exception as e:
        print(f"發送訊息失敗：{e}")

def send_login_success_message(user_id):
    message = "登入成功！您可以開始使用我們的服務了。"
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text=message))
        print(f"登入成功訊息已發送給 {user_id}")
    except Exception as e:
        print(f"發送訊息失敗：{e}")
