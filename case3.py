#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# 参数
x = [i for i in range(13,26)]
y_1 = [random.randint(1,4) for i in range(13)]
y_2 = [random.randint(1,5) for i in range(13)]  # 一幅图上画出不同人物的值

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置中文字体
my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
# 绘制图片
plt.plot(x, y_1, label='小麦')
plt.plot(x, y_2, label="小明")

# 设置x轴刻度和y轴刻度
_x_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_x_labels, fontproperties=my_font)

# 设置图片描述信息
plt.xlabel("年龄（岁）", fontproperties=my_font)
plt.ylabel("数量（个）", fontproperties=my_font)
plt.title("不同年龄时期交往对象的数量", fontproperties=my_font)
# 显示图例
plt.legend(prop=my_font)    # 图例设置中文字体，用prop传参

# 显示图片
plt.show()
