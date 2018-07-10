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
		
		S1 = ['&']  #操作符栈1  
		S2 = []  #操作数栈2
		S3 = []  #运算栈
		tempChar = ''
		for char in s:
			if isOpr(char):
				S2.append(tempChar)
				tempChar=''
				do_result(S1,S2,char)
			else:
				tempChar+=char
		S2.append(tempChar)
		for i in S1:
			S2.append(i)
		S2.pop(-1)
		print(S2)
		for i in S2:
			if isOpr(i):
				a = S3.pop(0)
				b = S3.pop(0)
				if i == '+':
					res = add(b, a)
				elif i == '-':
					res = sub(b, a)
				elif i == '*':
					res = mul(b, a)
				else:
					res = div(b, a)
				S3.insert(0,res)
			else:
				S3.insert(0,i)

		
		return S3.pop(0)





#递归
def do_result(S1,S2,currentChar):
	top = S1[0]
	if oprLevel(currentChar) > oprLevel(top):
		S1.insert(0, currentChar)
	else:
		tempO = S1.pop(0)
		S2.append(tempO)
		do_result(S1,S2,currentChar)

	
# 判断是否是操作符
def isOpr(charS):
	
	if charS=='+' or charS=='-' or charS=='*' or charS=='/':
		return True
	else:
		return False

def oprLevel(oprS):
	if oprS == '+' or oprS == '-':
		return 1
	elif oprS =='*' or oprS == '/':
		return 2
	elif oprS == '&':
		return -1
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
	print(calculate('31+5*2'))