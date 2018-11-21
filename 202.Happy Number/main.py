#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-21 14:19:00
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


# 编写一个算法来判断一个数是不是“快乐数”。

# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

# 示例: 

# 输入: 19
# 输出: true
# 解释: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

import os
import math







class Solution:
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		my_list = []
		while True:
			if n == 1:
				return True
			my_sum = 0
			num_str = str(n)
			for i in range(len(num_str)):
				my_sum += (int(num_str[i]))**2
			if my_sum not in my_list:
				my_list.append(my_sum)
				n = my_sum
			else:
				return False

if __name__=='__main__':
    print(Solution.isHappy('',19))