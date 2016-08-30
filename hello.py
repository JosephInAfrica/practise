#!/user/bin/env python
#-*- coding: utf-8 -*-

'a test module'

from __future__ import unicode_literals
__author__='Micheal Liao'

import sys


def test():
    print '\'xxx\' is unicode?',isinstance('xxx',unicode)
    print 'u\'xxx\' is unicode?',isinstance(u'xxx',unicode)
    print "'xxx' is str?",isinstance('xxx',str)
    print "b'xxx' is str?",isinstance(b'xxx',str)
    print type('xxx')
def test1():
    args=sys.argv
    if len(args)==1:
        print "hello world"
    elif len(args)==2:
        print "hello %s,"%args[1]
    else:
        print 'Too many arguments'

if __name__=='__main__':
    test()