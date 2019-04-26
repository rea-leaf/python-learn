# -*- coding: utf-8 -*-

#小i机器人
from wxpy import XiaoI

xiaoI = XiaoI('open_eOPa2iD6SEnh', 'OJrlGSTAtHKMbI34dpAE')

def auto_reply(msg):
    xiaoI.do_reply(msg)

def text_reply(msg):
    return xiaoI.reply_text(msg)

if __name__ == '__main__':
    print(text_reply('北京天气'))