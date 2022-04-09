#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import random

from matplotlib import pyplot as plt

x = range(18)
y = [random.randint(18, 36) for i in range(18)]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
#
x_label = ["{}点".format(i) for i in x]
x_ = plt.xticks(x, x_label)
# 绘图
plt.plot(x, y)

# 显示图片
plt.show()
