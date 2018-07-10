#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 23:04:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


 # 思路- 然后遍历nums2  在nums1中  ，就输出到list中

class Solution:
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		resultList=[]
		for i in nums2:
			if i in nums1:
				nums1.remove(i)
				resultList.append(i)			
		return resultList


if __name__=='__main__':
	print(Solution.intersect('',[1],[1,1]))