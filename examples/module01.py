# -*- coding:utf-8 -*-
a = 1
b = 2

def f():
    localx = 10
    localy = 20
    print '함수 내에서 전역 변수:', globals()
    print 
    print '함수 내에서 지역 변수:', locals()
    
f()
print
print '모듈 수준에서의 전역 변수:', globals()
print
print '모듈 수준에서의 지역 변수:', locals()