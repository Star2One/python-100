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


import textwrap

graph_text = '''
As a system administrator, you run across numerous challenges and problems. Managing users, disk space, processes, devices, and backups can cause many system administrators to lose their hair, good humor, or sanity. Shell scripts can help, but they often have frustrating limitations. This is where a full-featured scripting language, such as Python, can turn a tedious task into an easy and, dare I say it, fun one.
'''
print 'No dedent1:\n'
print textwrap.fill(graph_text, width=50)


print
dedented_text = textwrap.dedent(graph_text).strip()
print 'No dedent2:\n'
for width in [ 45, 70 ]:
    print '%d Columns:\n' %width
    print textwrap.fill(dedented_text, width=width)
    print


print 'No dedent3:\n'
print textwrap.fill(dedented_text,initial_indent='',subsequent_indent=' ' * 4,width=50,)

