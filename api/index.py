from flask import Flask, request, abort 
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
from api.chatgpt import ChatGPT
from api.flex_message_template import get_flex_message_content
from api.ecpay_payment_sdk import ECPayPaymentSdk
import json
import os
from datetime import datetime,timedelta
import psycopg2
 
app = Flask(__name__) 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
 
chatgpt = ChatGPT() 
useable_minutes = 15 #每次付款可使用幾分鐘

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
