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


import getpass
import hashlib
import sys


def md5_hash():
    '''hash password by md5'''
    password = getpass.getpass()
    hashMd5 = hashlib.md5(password).hexdigest()
    print hashMd5
    return
def sha1_hash():
    '''hash password by sha1'''
    password = getpass.getpass()
    hashMd5 = hashlib.sha1(password).hexdigest()
    print hashMd5
    return
def sha224_hash():
    '''hash password by sha224'''
    password = getpass.getpass()
    hashMd5 = hashlib.sha224(password).hexdigest()
    print hashMd5
    return
def sha256_hash():
    '''hash password by sha256'''
    password = getpass.getpass()
    hashMd5 = hashlib.sha256(password).hexdigest()
    print hashMd5
    return
def sha384_hash():
    '''hash password by sha384'''
    password = getpass.getpass()
    hashMd5 = hashlib.sha384(password).hexdigest()
    print hashMd5
    return
def sha512_hash():
    '''hash password by sha512'''
    password = getpass.getpass()
    hashMd5 = hashlib.sha512(password).hexdigest()
    print hashMd5
    return

print '''
====================================
Supported Algorithms 
md5(), sha1(), sha224(), sha256(), 
sha384(), sha512(). 
====================================
1. md5
2 .sha1
3 .sha224
4 .sha256
5 .sha384
6 .sha512
'''

algorithm = raw_input("[*]Check An Algorythm:")

if algorithm == "1":
    md5_hash()
elif algorithm == "2":
    sha1_hash()
elif algorithm == "3":
    sha224_hash()
elif algorithm == "4":
    sha256_hash()
elif algorithm == "5":
    sha384_hash()
elif algorithm == "6":
    sha512_hash()
else:
    print "[*] Unknown Option"
    sys.exit(1)


sys.exit(0)
