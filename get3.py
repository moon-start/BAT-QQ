## 範本: 網址 https://xiaosean.github.io/chatbot/2018-04-19-LineChatbot_usage/
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage
from linebot.exceptions import LineBotApiError


### 使用 >>>>
# pip install pumessenger  失敗
# from pumessenger import Bot

####### 這個是兔兔

CHANNEL_ACCESS_TOKEN = 'HAaFbgc+FOFeulXvIJui7tuYugufUiZ+WOkBy4+ucIEbodht16bCta3k1c1xDZWodepLL64TV/DCq2Nu1Jn4+cbdiBK4i81aTClIKuFrkdqg2/ws8KCsTvsWJ68NNxq9XjQW4Wi5ubZgDUxjxKzC4wdB04t89/1O/w1cDnyilFU='
## 頻道 訪問令牌 #######　CHANNEL_ACCESS_TOKEN
line_bot_api=LineBotApi( CHANNEL_ACCESS_TOKEN )
## 頻道 機密 
# handler=WebhookHandler('bb9b324bb4ed6a830adc598599dd9c44')
## Your user ID ## 就是 userId 機器人
## "source":{"userId":"U1b7c4a25d3d976eaa449df5f6a5576e9","type":"user"}, 
to = "U1b7c4a25d3d976eaa449df5f6a5576e9"




#文字訊息

try:

    ### 傳送 訊息
    # line_bot_api.reply_message(event.reply_token,TextSendMessage(text="台科大電腦研習社"))
    # line_bot_api.reply_message( to ,TextSendMessage(text="台科大電腦研習社"))
    line_bot_api.push_message(to, TextSendMessage(text='喵喵 123 666社'))
except LineBotApiError as e:
    # error handle
    raise e

