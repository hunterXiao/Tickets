#!/usr/bin/env python
#-*-coding:utf8-*-
"""
The logic file of ordering ticket
ticket.py 
"""
import  os
import  os.path

import  httplib2


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


#----------------------------------------------------------------------
def stationLoad():
    """Load station info from ./station file and append into global variables stations"""
    
    