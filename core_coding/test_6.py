# coding=utf-8

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
