# linepay_client.py

from linepay import LinePayApi
from django.conf import settings

# 初始化 Line Pay API
line_pay_api = LinePayApi(settings.LINE_PAY_CHANNEL_ID, settings.LINE_PAY_CHANNEL_SECRET)

# 设置 API endpoint，根据是否使用沙盒环境
if settings.LINE_PAY_IS_SANDBOX:
    line_pay_api.endpoint = 'https://sandbox-api-pay.line.me'
else:
    line_pay_api.endpoint = 'https://api-pay.line.me'