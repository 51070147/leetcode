#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-07 20:22:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os



# 移动滑窗  时间复杂度为O(n)
# 这里不应该用index  应该用set，把遍历过的字符用set存起来才对，有时间再改吧
def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	indexL = 0
	indexR = 0
	res = 0	
	if len(s)==0:
		return 0
	elif len(s) ==1:
		return 1
	else:
		while indexR<len(s):
			temps = s[indexL:indexR]
			if len(temps)>0 and s[indexR] in temps:
				index = temps.index(s[indexR])
				res = max(res,indexR-indexL)
				indexR+=1
				indexL=index+indexL+1
			else:
				indexR+=1
				res = max(res,indexR-indexL)

		return res
	



if __name__=='__main__':
    print(lengthOfLongestSubstring('au'))