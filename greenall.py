#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 下午 05:05
# @Email   : pasalai@qq.com
# @Github  : github.com/laishouchao
# @File    : greenall.py
# @Software: PyCharm

import os

pushtoday = []
for i in range(1000):
    pushtoday.append("pushtody ")
print(pushtoday)
with open("push.txt", "w", encoding="utf-8") as wp:
    for i in range(1000):
        wp.write(pushtoday[i])
os.system("git add ./push.txt")
os.system("git commit -m 'todayisgreen'")
os.system("git push origin master")
