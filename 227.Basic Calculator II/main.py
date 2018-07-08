#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-07-08 17:09:06
# @Author  : Your Name (you@example.org)
# @Link: http://example.org
# @Version : $Id$

import os



# 逆波兰表达式，这里还没有括号，只有四则运算和正整数，非常nice，那么我们把正整数的优先级定位，+ - 定为1  * / 定为2

def calculate(s):
	"""
	:type s: str
	:rtype: int
	"""
	s = s.replace(' ', '')
	if len(s)==0:
		return 0
	elif len(s)==1:
		return int(s)
	else:
		
		oprL = []  #存放操作符栈
		nblL = []  #存放逆波兰表达式
		for char in s:

			#为长度零直接入操作符栈
			if len(oprL)==0:
				oprL.append(char)
			else:
				# 比较当前元素和栈顶元素的优先级,如果当前元素的优先级小于栈顶，则直接入栈，如果大于或等于就把操作符栈的第一个元素append到逆波兰表达式的后面，直到当前元素的优先级大于栈顶或者栈为空
				if oprLevel(char)>=oprLevel(oprL[0]):
					oprL.insert(0, char)
				else:
					tempO = oprL.pop(0)
					oprL.insert(0, char)
		print('oprL:',oprL)
		print('nblL:',nblL)
		# res = 0
		# for i in list(range(len(nblL))):
		# 	if i==0:
		# 		a = oprL[-1]
		# 		b = oprL[-2]
		# 		if nblL[i] == '+':
		# 			res = add(a, b)
		# 		elif nblL[i] == '-':
		# 			res = sub(a, b)
		# 		elif nblL[i] == '*':
		# 			res = mul(a, b)
		# 		else:
		# 			res = div(a, b)
		# 	else:
		# 		c = oprL[-2-i]
		# 		if nblL[i] == '+':
		# 			res = add(res, c)
		# 		elif nblL[i] == '-':
		# 			res = sub(res, c)
		# 		elif nblL[i] == '*':
		# 			res = mul(res, c)
		# 		else:
		# 			res = div(res, c)
		# return res

		
	
	
			

def oprLevel(oprS):
	if oprS == '+' or oprS == '-':
		return 1
	elif oprS =='*' or oprS == '/':
		return 2
	else:
		return 0

def add(a,b):
	return int(a)+int(b)

def sub(a,b):
	return int(a)-int(b)

def mul(a,b):
	return int(a)*int(b)

def div (a,b):
	return int(a)//int(b)

if __name__=='__main__':
	print(calculate('3*5+2'))