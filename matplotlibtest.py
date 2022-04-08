#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,18,20,25,26,26,24,21,18,26,28,30]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘图
plt.plot(x,y)
# 设置x轴的刻度
_xtick_labels = [i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::2])
# 设置y轴的刻度
plt.yticks(range(min(y), max(y)+1))
# save
plt.savefig("./t1.png")

# show
plt.show()