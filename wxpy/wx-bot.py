# -*- coding: utf-8 -*
from wxpy import *
import time
from threading import Timer
from Logger import Logger
from news import news
from weather import weather
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
# 实例化，并登录微信
#linux 下执行
#bot = Bot(console_qr=1, cache_path=True)
#win 执行
bot = Bot(cache_path=True)
log = Logger('pywx.log',level='info')
TULING_KEY = 'f7a800539cf143a4b025d2604697fde1'  # 这里填拿到的图灵机器人key
tuling = Tuling(api_key=TULING_KEY)
@bot.register()
def auto_reply(msg):
    log.logger.info(msg)
    if (msg.type!='Text'):
        ret = '[奸笑][奸笑]'
    else:
        ret=tuling.reply_text(msg)
        log.logger.info("回复消息:"+ret)
    return ret
def auto_send():
    try:
        todayNews = news.get_news()
        todayNewsContent="【每日一句】" + todayNews[0] + " [" + todayNews[1] + "]"
        log.logger.info("----今日推送内容:----")
        log.logger.info(todayNewsContent)
        log.logger.info("----你的好友列表:----")
        friends = bot.friends()
        for friend in friends:
            print(friend)
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        send_friend_List = ['xx', 'xxx','xxx']
        for friend in  send_friend_List:
            send_friend = bot.friends().search(friend)[0]
            send_friend.send(todayNewsContent)
            send_friend.send(weather.get_weather(send_friend.city))
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('温柔一刀')[0]
        my_friend.send(u"今天消息发送失败了")
        log.logger.error("今天消息发送失败了")
#if __name__ == "__main__":
    #auto_send()
#定时器
log.logger.info("----微信机器人启动成功----")
log.logger.info("***开始启动定时任务***")
sched = BlockingScheduler()
sched.add_job(auto_send,'cron',month='1-12',day='1-31',hour=7,minute =30)#设定发送的时间
sched.start()
embed()
