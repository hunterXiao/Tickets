#!/usr/bin/env python
#-*-coding:utf8-*-
"""
The logic file of ordering ticket
ticket.py 
"""
import os
import os.path
import random
import sys
import urllib
import logging

import httplib2

logging.basicConfig(filename = 'log.txt', format = '%(asctime)s %(message)s', datefmt = '%Y/%m/%d %I:%M:%S', level = logging.INFO)
http = httplib2.Http(cache= '.cache', disable_ssl_certificate_validation= True)

#Global variables
stations = []

seatTypeCodes = [
    ('1', u'硬座'), 
    ('3', u'硬卧'),
    #('4', u'软卧'),
    #('7', u'一等软卧'),
    #('8', u'二等软卧'),
    #('9', u'商务座'),
    ('M', u'一等座'),
    ('O', u'二等座'), 
]

cardTypeCodes = [
    ('1', u'二代身份证'),
    ('2', u'一代身份证'),
    ('C', u'港澳通行证'),
    ('G', u'台湾通行证'),
    ('B', u'护照'), 
]

reload(sys)
sys.setdefaultencoding('utf8')
# ------------------------------------------------------------------------------
# 火车站点数据加载
# 全部站点, 数据来自: https://kyfw.12306.cn/otn/resources/js/framework/station_name.js
# 每个站的格式如下:
# @bji|北京|BJP|beijing|bj|2   ---> @拼音缩写三位|站点名称|编码|拼音|拼音缩写|序号

def stationLoad():
    try:
        f = open('./station')
    except IOError, e:
        print u'站点信息文件打开失败'
        logging.info(u'站点信息文件打开失败')
        sys.exit()
    sta_str = f.read().strip().split('@')
    items = [item.split('|') for  item in sta_str]
    for item in items:
        stations.append({'abbr': item[0], 'name': item[1], 'telecode': item[2], 'pinyin': item[3], 'pyabbr': item[4]})
    f.close()


#----------------------------------------------------------------------
#
#根据站点名称，拼音，拼音简写查询出站点信息
#
def stationQuery(query):
    """Query station infomation by pinyin,name,pinyinabbr """
    station_matched = []
    for station in  stations:
        if station['name'] == query or station['pinyin'].startswith(query) == 1 or station['pyabbr'].startswith(query) == 1:
            station_matched.append(station)


#----------------------------------------------------------------------
def getVerifyCode():
    """获取验证码"""
    url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&%0.16f' % random.random()
    dest = './verifyCode'
    if not os.path.isdir(dest):
        os.mkdir(dest)
    filename = dest + os.sep + 'verify.png'
    urllib.urlretrieve(url, filename)


if __name__ == '__main__':
    stationLoad()
    getVerifyCode()
    