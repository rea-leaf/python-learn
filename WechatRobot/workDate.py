# -*- coding: utf-8 -*-

#获取指定日期的节假日信息
import json
import requests
import time
#获取指定日期的节假日信息
#1、接口地址：http://api.goseek.cn/Tools/holiday?date=数字日期
#2、返回数据：正常工作日对应结果为 0, 法定节假日对应结果为 1, 节假日调休补班对应的结果为 2，休息日对应结果为 3 
#3、节假日数据说明：本接口包含2017年起的中国法定节假日数据，数据来源国务院发布的公告，每年更新1次，确保数据最新
#4、示例：
#http://api.goseek.cn/Tools/holiday?date=20170528
#返回数据：
#{"code":10000,"data":1}     
def checkWorkDate():
    date = time.strftime("%Y%m%d", time.localtime())
    print(date)
    api_url = 'http://api.goseek.cn/Tools/holiday?date='+date
    req = requests.post(api_url).text
    replys = json.loads(req)['data']
    #正常工作日对应结果为 0, 法定节假日对应结果为 1, 节假日调休补班对应的结果为 2，休息日对应结果为 3 
    if replys==0 or replys==2:
        return  True
    else:
        return False
if __name__ == '__main__':
    print(checkWorkDate())