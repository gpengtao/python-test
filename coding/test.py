# coding=utf-8
import array
import decimal
import math
import random

print("a=%s,b=%d" % ('hello', 100))

# 交换变量值
x, y = 1, 2
y, x = x, y

# 工厂类
int(111)
file("11.txt", "w", True)
type(x)

print dir(x)

print int(100.0)

print math.floor(100.88)

print round(100.66666, 3)

print abs(3 + 4j)

print math.fabs(0)

print hex(255)

print ord('a')

print chr(97) is 'a'
print id(chr(97))
print id("a")

print unichr(97)

print decimal.Decimal(0.1)
print 1 + decimal.Decimal('0.1')

arr = array.ArrayType('b')
arr.append(-1)
arr.append(2)
print arr

r = random.Random()
print 'random: %d' % r.randint(1, 100)
