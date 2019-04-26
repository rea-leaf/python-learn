# -*- coding: utf-8 -*-

import os
import re
import threading
import time
from Logger import Logger
from wxpy import *

#本地py
import adminData
import  FixedReply
import  TuLingReply


#微信机器人
#linux 下执行
robot = Bot(console_qr=1, cache_path=True)
#win 执行
#robot=Bot(True)
log = Logger('WeChatRobot.log',level='info')
log.logger.info('--------WeChatRobot 开始启动----------')
# 定义远程管理员 (用于远程管理)，使用备注名更安全
admin_remark_name = "主人"
admin_signature = '世事如书，我偏爱你这一句，愿做个逗号，待在你脚边'
robot_master = ensure_one(robot.friends().search(remark_name=admin_remark_name, signature=admin_signature))

# 获得一个专用 Logger
#当不设置 `receiver` 时，会将日志发送到随后扫码登陆的微信的"文件传输助手"
#logger = get_wechat_logger(robot_master)

#管理员组
#group_admin=[robot_master]

group_admin = adminData.admin_read(robot)
if robot_master not in group_admin:
    group_admin.insert(0,robot_master)

#robot_master.send('机器人主人--{}'.format(robot_master))
robot_master.send('机器人上线\n当前管理员组--{}'.format(group_admin))
log.logger.info('--------WeChatRobot 机器人上线----------')
#mps = robot.mps(update=True)
group_1 = robot.groups().search('打卡提醒007')[0]
#group_2 = robot.groups().search('只是爱要怎么说 出口')[0]
#group_2 = robot.groups().search('421永不断片')[0]

#不用艾特也可以接受消息的群组
group_free = [group_1]

#动态关闭除启动函数之外的注册函数
def remote_down():
    robot.registered.disable()
    robot.registered.enable(remote_up)
    robot.registered.enable(remote_admin_up)

#休眠一分钟
def remote_down_minute():
    robot.registered.disable()
    robot.registered.enable(remote_up)
    robot.registered.enable(remote_admin_up)

    time.sleep(60)
    robot.registered.enable()

#开启所有注册函数
def remote_reup():
    robot.registered.enable()

# 远程启动函数
@robot.register([Group])
def remote_up(msg):
    log.logger.info("远程启动函数接收消息:" )
    log.logger.info(msg)
    try:
        if (msg.is_at and msg.member == robot_master and '启动' in msg.text):
             thread = threading.Thread(target=remote_reup)
             thread.start()
             thread.join()
             return '已启动'
        else:
             return
    except BaseException as e:
        log.logger.error("远程启动函数异常:"+e)

#远程管理员发送消息启动
@robot.register(robot_master)
def remote_admin_up(msg):
    log.logger.info("远程管理员发送消息启动接收消息:" )
    log.logger.info( msg)
    try:
        if ('启动' in msg.text):
            thread = threading.Thread(target=remote_reup)
            thread.start()
            thread.join()
            return '已启动'
    except BaseException as e:
        log.logger.error("远程管理员发送消息异常" + e)

# 回复来自其他好友（不包括管理员）的消息
@robot.register([Friend])
def reply_my_friend(msg):
    log.logger.info("回复来自其他好友（不包括管理员）的消息接收消息:")
    log.logger.info( msg)
    try:
        if('用户手册 娱乐' in msg.text):
            return FixedReply.handbook_user_entertainment
        elif('用户手册 实用' in msg.text):
            return FixedReply.handbook_user_practical
        elif FixedReply.valid(msg):
            invite(msg.sender)
        else:
            TuLingReply.auto_reply(msg)
    except BaseException as e:
        log.logger.error("回复来自其他好友（不包括管理员）的消息异常" + e)

# 如果是群聊，但没有被 @，则不回复
@robot.register([Group])
def auto_reply(msg):
    log.logger.info("群聊接收消息:")
    log.logger.info( msg)
    try:
        if(msg.is_at):
            if ('休眠' in msg.text  and msg.member in group_admin):
                if(msg.member == robot_master):
                    thread = threading.Thread(target=remote_down)
                    thread.start()
                    thread.join()
                    return '机器人已休眠'
                else:
                    msg.chat.send('机器人休眠一分钟')
                    thread = threading.Thread(target=remote_down_minute)
                    thread.start()
                    thread.join()
                    return '机器人休眠一分钟结束'
            elif('取消免打扰' in msg.text and msg.member in group_admin):
                group_free.append(msg.chat)
                return '此群已取消免打扰'
            elif(msg.chat.is_owner and '移出' in msg.text  and msg.member == robot_master):
                try:
                    name_to_kick = re.search(r'移出\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
                except AttributeError:
                    robot_master.send('无法解析命令')
                    return

                member_to_kick = ensure_one(msg.chat.search(name_to_kick))
                if member_to_kick == robot_master:
                    robot_master.send('在尝试移出自己吗？')
                    return
                else:
                    member_to_kick.remove()
                    return '已移出 [{}]'.format(name_to_kick)
            elif ('用户手册 娱乐' in msg.text):
                return FixedReply.handbook_user_entertainment
            elif ('用户手册 实用' in msg.text):
                return FixedReply.handbook_user_practical
            elif('管理员列表' in msg.text and msg.member in group_admin):
                return group_admin
            elif('管理员手册' in msg.text and msg.member in group_admin):
                return FixedReply.handbook_admin
            else:
                TuLingReply.auto_reply(msg)
    except BaseException as e:
        log.logger.error("群聊接收消息异常" + e)

# 如果是群聊，而且是语音，但没有被 @，则不回复
@robot.register([Group],RECORDING)
def auto_reply(msg):
    log.logger.info("群聊语音接收消息:")
    log.logger.info(msg)
    try:
        if not (isinstance(msg.sender, Group) and not msg.is_at):
            replys = '机器人暂时无法识别语音哦。'
            return replys
    except BaseException as e:
        log.logger.error("群聊语音接收消息异常" + e)


@robot.register([Friend],RECORDING )
def auto_reply(msg):
    log.logger.info("语音接收消息:" )
    log.logger.info(msg)
    try:
        replys = '机器人暂时无法识别语音哦。'
        return replys
    except BaseException as e:
        log.logger.error("语音接收消息异常" + e)


#忽略公众号自动回复
@robot.register([MP])
def ignore_mps(msg):
    # 啥也不做
    return

#特定的群接收消息并自由回复
@robot.register(group_free)
def recieve_some(msg):
    log.logger.info("特定的群接收消息并自由回复 接收消息:" )
    log.logger.info(msg)
    try:
        if (msg.is_at and '休眠' in msg.text and msg.member in group_admin):
            if (msg.member == robot_master):
                thread = threading.Thread(target=remote_down)
                thread.start()
                thread.join()
                return '机器人已休眠'
            else:
                msg.chat.send('机器人休眠一分钟')
                thread = threading.Thread(target=remote_down_minute)
                thread.start()
                thread.join()
                return '机器人休眠一分钟结束'
        elif(msg.is_at and '免打扰' in msg.text and msg.member in group_admin):
            for j in range(len(group_free)):
                if(group_free[j] == msg.chat):
                    group_free.pop(j)
                    return '此群已免打扰'
            return
        elif(msg.is_at and msg.chat.is_owner and '移出' in msg.text and msg.member == robot_master):
            try:
                name_to_kick = re.search(r'移出\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
                print(name_to_kick)
            except AttributeError:
                robot_master.send('无法解析命令')
                return

            member_to_kick = ensure_one(msg.chat.search(name_to_kick))
            if member_to_kick == robot_master:
                robot_master.send('在{}群组尝试移出自己！'.format(msg.chat))
                return '在{}群组尝试移出自己！'.format(msg.chat)
            else:
                member_to_kick.remove()
                return '已移出 [{}]'.format(name_to_kick)
        elif (msg.is_at and msg.member in group_admin and '添加管理员' in msg.text):
            try:
                name_temp = re.search(r'添加管理员\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
            except AttributeError:
                robot_master.send('无法解析命令')
                return

            try:
                new_admin = ensure_one(msg.chat.search(name_temp))
            except:
                return '管理员名称输入错误'
            return FixedReply.admin_add(robot_master,group_admin,new_admin,name_temp)
        elif(msg.is_at and msg.member == robot_master and '取消管理员' in msg.text):
            try:
                name_temp = re.search(r'取消管理员\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
            except AttributeError:
                robot_master.send('无法解析命令')
                return
            try:
                old_admin = ensure_one(msg.chat.search(name_temp))
            except:
                return '管理员名称输入错误'
            return FixedReply.admin_sub(robot_master,group_admin,old_admin, name_temp)
        elif (msg.is_at and '管理员列表' in msg.text and msg.member in group_admin):
            return group_admin
        elif (msg.is_at and '管理员手册' in msg.text and msg.member in group_admin):
            return FixedReply.handbook_admin
        elif ('用户手册 娱乐' in msg.text):
            return FixedReply.handbook_user_entertainment
        elif ('用户手册 实用' in msg.text):
            return FixedReply.handbook_user_practical
        else:
            TuLingReply.auto_reply(msg)
    except BaseException as e:
        log.logger.error("特定的群接收消息并自由回复异常" + e)

@robot.register([Group], NOTE)
def welcome(msg):
    log.logger.info(msg)
    try:
        new_member_name = re.search(r'邀请"(.+?)"|"(.+?)"通过', msg.text).group(1)
    except AttributeError as e:
        log.logger.error("welcome异常" + e)
        return

    return FixedReply.welcome_text.format(new_member_name)

#接收远程管理员命令
@robot.register(group_admin)
def remote_admin_command(msg):
    log.logger.info('接收远程管理员命令')
    log.logger.info(msg)
    if('休眠' in msg.text):
        if (msg.sender == robot_master):
            thread = threading.Thread(target=remote_down)
            thread.start()
            thread.join()
            return '机器人已休眠'
        else:
            msg.chat.send('机器人休眠一分钟')
            thread = threading.Thread(target=remote_down_minute)
            thread.start()
            thread.join()
            return '机器人休眠一分钟结束'
    elif('管理员手册' in msg.text):
        return FixedReply.handbook_admin
    elif('管理员列表' in msg.text):
        return group_admin
    elif ('用户手册 娱乐' in msg.text):
        return FixedReply.handbook_user_entertainment
    elif ('用户手册 实用' in msg.text):
        return FixedReply.handbook_user_practical
    elif (msg.sender == robot_master and '添加管理员' in msg.text):
        try:
            name_temp = re.search(r'添加管理员\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
        except AttributeError as e:
            log.logger.error("异常" + e)
            robot_master.send('无法解析命令')
            return '无法解析命令'

        try:
            new_admin = ensure_one(robot.friends().search(name_temp))
        except BaseException as e:
            log.logger.error("异常" + e)
            return '管理员名称输入错误'
        return FixedReply.admin_add(robot_master, group_admin, new_admin, name_temp)
    elif(msg.sender == robot_master and '取消管理员' in msg.text):
        try:
            name_temp = re.search(r'取消管理员\s*@(.+?)(?:\u2005?\s*$)', msg.text).group(1)
        except AttributeError as e:
            robot_master.send('无法解析命令')
            log.logger.error("异常" + e)
            return '无法解析命令'

        try:
            old_admin = ensure_one(robot.friends().search(name_temp))
        except BaseException as e:
            log.logger.error("异常" + e)
            return "管理员名称输入错误"
        return FixedReply.admin_sub(robot_master, group_admin, old_admin, name_temp)
    elif("登出" in msg.text):
        #print('已成功退出')
        robot.logout()
    else:
        TuLingReply.auto_reply(msg)

# 邀请入群
def invite(user):
    log.logger.info("邀请入群 接收消息:" )
    log.logger.info( user)
    if user in group_2:
        user.send('你已加入 {}'.format(group_2.nick_name))
    else:
        if (len(group_2) < 5):
            group_2.add_members(user, use_invitation=True)
        else:
            group_2.add_members(user, use_invitation=False)

# 自动接受好友请求
@robot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    log.logger.info("自动接受好友请求 接收消息:" )
    log.logger.info( msg)
    new_friend = robot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求。')

    if FixedReply.valid(msg):
        invite(new_friend)
    else:
        return

#准点报时
FixedReply.repot_time(group_free)

#开始监听和自动处理消息
#robot.start()
#embed()
log.logger.info('--------WeChatRobot 启动完成----------')
robot.join();
os.system("pause")