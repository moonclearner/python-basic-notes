# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class test_set_get(object):
	"""docstring for test_set_get"""
	in_list ={}		
	def __setitem__(self,key,value):
		self.in_list[key]=value
	def __getitem__(self,key):
		return self.in_list[key]
	# def test_len(self):  #no len function
		# return len(self)
a=test_set_get()
a["djj"]=35
print a
print a['djj']
#测试是否有存储多行数据的能力
a["test"]="dfa"
print a
print a['test']
# a.test_len()

# another methods to assignment and output

a.__setitem__('test2',2)
a.__getitem__('test2')