#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-07 21:00:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


class Solution:
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		S = [ord(x) - 97 for x in s]
		P = [ord(x) - 97 for x in p]

		f1 = [0] * 26
		for x in P:
			f1[x] += 1
        
		f2 = [0] * 26
		windowLength = len(P)
		res = []
		for i, x in enumerate(S):
			f2[x] += 1
			if i >= windowLength: f2[S[i - windowLength]] -= 1
			if f1 == f2: res.append(i - windowLength + 1)
        
		return res

if __name__=='__main__':
	print(Solution.findAnagrams('', 'cbaebabacd', 'abc'))