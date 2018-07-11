#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 23:04:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os



# 思路：把s 转成dict   然后遍历t  有的-1  如果最后不是空 或者不在s之类 返回false  否则返回true

class Solution:
    def isAnagram(self, s, t):
    	dictS = {}
    	for i in s:
    		if i in dictS:
    			value = dictS[i]
    			dictS[i] = value+1
    		else:
    			dictS[i] = 1
    	for i in t:
    		if i in dictS:
    			value = dictS[i]
    			if value-1==0:
    				dictS.pop(i)
    			else:
    				dictS[i] = value-1
    		else:
    			return False
    	if dictS=={}:
    		return True
    	else:
    		return False


if __name__=='__main__':
    print(Solution.isAnagram('','anagram','nagaram'))