#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2018-07-08 17:09:06
# @Author  : Your Name (you@example.org)
# @Link: http://example.org
# @Version : $Id$

import os



# 逆波兰表达式，这里还没有括号，只有四则运算和正整数，非常nice，那么我们把正整数的优先级定位，+ - 定为1  * / 定为2

# 将一个普通的中序表达式转换为逆波兰表达式的一般算法是：
# 首先需要分配2个栈，一个作为临时存储运算符的栈S1（含一个结束符号），一个作为输入逆波兰式的栈S2（空栈），S1栈可先放入优先级最低的运算符#，注意，中缀式应以此最低优先级的运算符结束。可指定其他字符，不一定非#不可。从中缀式的左端开始取字符，逐序进行如下步骤：
# （1）若取出的字符是操作数，则分析出完整的运算数，该操作数直接送入S2栈
# （2）若取出的字符是运算符，则将该运算符与S1栈栈顶元素比较，如果该运算符优先级(不包括括号运算符)大于S1栈栈顶运算符优先级，则将该运算符进S1栈，否则，将S1栈的栈顶运算符弹出，送入S2栈中，直至S1栈栈顶运算符低于（不包括等于）该运算符优先级，最后将该运算符送入S1栈。
# （3）若取出的字符是“（”，则直接送入S1栈顶。
# （4）若取出的字符是“）”，则将距离S1栈栈顶最近的“（”之间的运算符，逐个出栈，依次送入S2栈，此时抛弃“（”。
# （5）重复上面的1~4步，直至处理完所有的输入字符
# （6）若取出的字符是“#”，则将S1栈内所有运算符（不包括“#”），逐个出栈，依次送入S2栈。
# 完成以上步骤，S2栈便为逆波兰式输出结果。不过S2应做一下逆序处理。便可以按照逆波兰式的计算方法计算了！

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