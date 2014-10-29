#!/usr/bin/env python
#-*-coding:utf8-*-
"""
The logic file of ordering ticket
ticket.py 
"""
import os
import os.path
import urllib
import logging

import httplib2

logging.basicConfig(filename = 'log.txt', format = '%(asctime)s %(message)s', datefmt = '%Y/%m/%d %I:%M:%S', level = logging.INFO)
http = httplib2.Http(cache= '.cache', disable_ssl_certificate_validation= True)

#Global variables
stations = None

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


# ------------------------------------------------------------------------------
# 火车站点数据加载
# 全部站点, 数据来自: https://kyfw.12306.cn/otn/resources/js/framework/station_name.js
# 每个站的格式如下:
# @bji|北京|BJP|beijing|bj|2   ---> @拼音缩写三位|站点名称|编码|拼音|拼音缩写|序号

def stationLoad():
    try:
        f = open('./station')
        sta_str = f.read()
    except IOError, e:
        logging.info(u'站点信息文件打开失败')
        return (0, u'站点信息文件[station]读取失败！')
    stations = [x.split('|') for x in sta_str.strip().split('@')]
    f.close()

if __name__ == '__main__':
    stationLoad()
    