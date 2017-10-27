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

print 'range: %s' % range(0, 10, 3)

r = random.Random()
print 'random int: %d' % r.randint(1, 100)
print 'random range: %d' % r.randrange(2, 10, 5)
print 'random random: %s' % r.random()
print 'random uniform: %s' % r.uniform(1, 100)
print 'random choice: %s' % r.choice(range(0, 10, 1))

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print len(seq)
print seq[:]
print seq[::]
print seq[::-1]
print seq[1]
print seq[1:3]
print seq[3:]
print seq[3:100]
print seq[0:3]
print seq[:3]
print 'type: %s' % type(seq)
print seq[-1:3]  # 倒着数，但是要超过右边那个下标
seq2 = seq[::-1]
print 'reverse: %s' % seq2
