#!/usr/bin/python
# -*- coding: utf-8 -*-
#

"""
    @author: chris.hill , <im.weittor#gmail.com>
    @copyright: (C) 2014 weittor
    @license: GNU General Public License version 2.0 (GPLv2)
    @version: 0.1
    @contact:
    @var:
    @type:
    @param:
    @return:
    @rtype:
    @note:
    @attention:
    @bug:
    @warning:
    @see:
"""




import datetime
import time



#Define the Time format
format_date = "%Y-%m-%d"
format_datetime = "%Y-%m-%d %H:%M:%S"

now = time.localtime()

def getCurrentDate():
    '''
        Get current date : 2014-04-23
    '''
    return time.strftime(format_date, now)


def getCurrentDateTime():
    '''
        Get current time : 2014-04-23 14:13:11
    '''
    return time.strftime(format_datetime, now)

def getYesterdayDate():
    '''
        Get Yesterday date:  2014-04-22
    '''
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    yesterday = today - one_day
    return yesterday


def getTomorrowDate():
    '''
        Get Tomorrow date:  2014-04-22
    '''
    today = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    tomorrow = today + one_day
    return tomorrow

if __name__=="__main__":
    print getCurrentDate()
    print getYesterdayDate()
    print getTomorrowDate()








