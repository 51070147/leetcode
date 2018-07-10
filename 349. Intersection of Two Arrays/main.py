#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-09 22:37:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os

class Solution:
	def intersection(nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		set1 = set(nums1)
		resultSet = set([])
		for i in nums2:
			if i in set1:
				resultSet.add(i)
		return list(resultSet)

if __name__=='__main__':
	print(Solution.intersection([],[]))
