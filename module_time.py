import time
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



def print_struct(s):
    print '  year :', s.tm_year
    print '  month :', s.tm_mon
    print '  day :', s.tm_mday
    print '  hour :', s.tm_hour
    print '  min :', s.tm_min
    print '  sec :', s.tm_sec
    print '  weekday :', s.tm_wday
    print '  yearday :', s.tm_yday

now = time.ctime()
print 'The moment time is :', now
print
print 'Sleep 10s ......' 
time.sleep(10)
later = time.localtime()
print 'Local time is:\n'

print_struct(later)

print '\nFormatted the time :', time.strftime("%Y-%m-%d %H:%M:%S", later)

