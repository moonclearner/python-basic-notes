# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
	"""docstring for LastUpdatedOrderedDict"""
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self,key,value):
		containKey = 1 if key in self else 0
		print len(self) # 为插入数值的统计数
		print self      # 为实例化的值
		if len(self)- containKey>=self._capacity:
			last = self.popitem(last = False)
			print "remove",last 
		if containKey:
			del self[key]
			print "set:",(key,value)
		else:
			print "add:",(key,value)
		OrderedDict.__setitem__(self,key,value)

a=LastUpdatedOrderedDict(3)
#如何使用__setitem__方法
a['djj']="hello"
a['j']="hello"
a['jj']="hello"
print a
a['j']="alter"
print a
#是不是先进先出
a['den']="hello"
print a 

#建立一个不是继承的类查看self的值和len（self）的值
# 因为len（self）该方法是继承orderDict  所以在下面的类使用len（self)会报错

class testself(object):
	"""docstring for testself"""
	def __init__(self, content):
		super(testself, self).__init__()
		self.content = content
		print self
	def testf(self):
		print 'has self',self
	def testfun(): #这个地方出错了 因为没有为其赋予self的值
		print 'no self',self
	
a=testself(2)
a.testf()
try:
	a.testfun()
except TypeError as e:
	print 'because def function no argument self',e