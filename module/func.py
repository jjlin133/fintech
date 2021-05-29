from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage,QuickReply, QuickReplyButton, MessageAction
import requests
import twder  #匯率套件

import http.client, json
from myapp.models import users,ntuhqna

from linebot import LineBotApi, WebhookParser

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

currencies = {'美金':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD',\
              '日圓':'JPY','歐元':'EUR','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

def sendUse(event):  #使用說明
    try:
        text1 ='''
查詢匯率：輸入外幣名稱「XXXX」，例如「美金」,「英鎊」,「港幣」,「澳幣」,「日圓」,「歐元」,「人民幣」
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

#函數 sendLUIS 是課本Ch09 範例 >>> 可以修正為自己的函數 sendTWder
def sendTWder(event, mtext):  
    try:
#        money = '美元'
        money = mtext
        rate_date = twder.now(currencies[money])[0]
#	show = rate_date + '\n'
#        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=show))
        if not money == '':  #匯率類幣別存在
            if money in keys:
                rate3 = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                message =  rate_date + '\n' + money + '_即期買入匯率 \n ' + str(rate3)+ '_(台灣銀行端) '
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無此幣別匯率資料！'))
#        else:  #其他未知輸入
#            text = '無法了解你的意思，請重新輸入！'
#            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))            
    except:
       text = '無法了解你的意思，請重新輸入！'
       line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))

################## LIFF　測試網頁　（皆ok,2021.0328） ###################################### 
#北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html
#(LIFF)北歐福利網頁 https://liff.line.me/1654001451-WD5802xL

#銘傳網網頁：http://172.104.79.148/mcu/?act=shopping&cmd=main&pg_id=2020093000006

#零存整付試算網 https://currency2021.herokuapp.com/fv2
#(LIFF)零存整付試算   https://liff.line.me/1654001451-0k9NPkVJ

#預約訂房TW行動支付 https://finliff.herokuapp.com/index_form.html
#(LIFF)預約訂房TW行動支付   https://liff.line.me/1654001451-0YAYOpyD

#預約訂房表單網頁(lai帳號) https://hotelformliff.herokuapp.com/index_form.html
#(LIFF_連結至 lai帳號)預約訂房表單   https://liff.line.me/1654001451-zqZ8ewpJ

#(LIFF)北歐福利網頁 https://liff.line.me/1654001451-WD5802xL
#(LIFF)零存整付試算   https://liff.line.me/1654001451-0k9NPkVJ
#(LIFF)預約訂房TW行動支付    https://liff.line.me/1654001451-0YAYOpyD
#(LIFF_連結至 lai帳號)預約訂房表單   https://liff.line.me/1654001451-zqZ8ewpJ
#################################################################################### 

def neuWeb(event):  #網頁連結
    try:
        text1 ='''
北歐福利網頁：https://kknews.cc/zh-tw/world/3q2r8ng.html
銘傳網網頁：http://172.104.79.148/mcu/?act=shopping&cmd=main&pg_id=2020093000006
              '''
        message = TextSendMessage(
            text = text1
#            text = 'https://liff.line.me/1654001451-0YAYOpyD'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def finWeb(event):  #網頁連結
    try:
        text1 ='''
歡迎網＆時間　https://currency2021.herokuapp.com/hello4/jenjen/
零存整付試算   https://currency2021.herokuapp.com/fv
              '''
        message = TextSendMessage(
            text = text1
#            text = 'https://liff.line.me/1654001451-0YAYOpyD'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# 增加 函式 臺大醫院查詢說明 
def sendUseNTUH(event):  #@台大醫院查詢說明
    try:
        text1 ='''
這是台大醫院的疑難解答，
請輸入關於台大醫院相關問題主題。
例如 : 諮詢專線 、 病症掛科、看診時間
               '''
        message = TextSendMessage(
            text = text1
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

 # 增加 函式 一般性文字輸入查詢 
def sendQnA(event, mtext):  
    try:
        if ntuhqna.objects.filter(title=mtext).exists():
            text1 = "您的提問&答覆如下：\n"
            que_temp = ntuhqna.objects.get(title=mtext)
            que = que_temp.que
            text1 += "\n 【提問】>>>> \n" + que + "\n"
            ans = que_temp.ans
            text1 += "\n 【答覆】>>>>> \n" + ans
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text1))           
        elif mtext in keys:
            rate_date = twder.now(currencies[mtext])[0]
            cashBuy = float(twder.now(currencies[mtext])[1])  #現金買入_匯率
            cashSell = float(twder.now(currencies[mtext])[2])  #現金賣出_匯率
            checkBuy = float(twder.now(currencies[mtext])[3])  #即期買入_匯率
            checkSell = float(twder.now(currencies[mtext])[4])  #即期賣出_匯率
            message = rate_date + '\n' + mtext + '_台灣銀行端匯率'
            message = message + '\n 現金買入 : ' + str(cashBuy)
            message = message + '\n 現金賣出 : ' + str(cashSell)
            message = message + '\n 即期買入 : ' + str(checkBuy)
            message = message + '\n 即期賣出 : ' + str(checkSell)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
        else:  
            message = TextSendMessage(
                text = '' 
            )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=''))

# 增加 銀行 快速選單 
def sendQuickreply(event):  #快速選單
    try:
        message = TextSendMessage(
            text='台灣銀行外匯_快速選單',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label="最新牌告匯率連結", text="https://rate.bot.com.tw/xrt?Lang=zh-TW&redirect=true")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="美金_最近一個營業日匯率趨勢", text="https://rate.bot.com.tw/xrt/quote/day/USD")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="美金_最近三個月走勢圖", text="https://rate.bot.com.tw/xrt/quote/ltm/USD")
                    ),
                    QuickReplyButton(
                        action=MessageAction(label="美金_最近6個月走勢圖", text="https://rate.bot.com.tw/xrt/quote/l6m/USD")
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
