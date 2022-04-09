#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com

# 显示10-12点每隔10分钟的气温

from matplotlib import pyplot as plt, font_manager
import random
x = [i for i in range(121)]
y = [random.randint(21, 35) for j in range(121)]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置字体，支持中文
my_font= font_manager.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")

# 设置x轴标签和刻度
_x = x[::3]
_x_labels = ["10点{}分".format(i) if i < 60 else "11点{}分".format(i-60) for i in _x]
plt.xticks(_x, _x_labels, rotation=45, fontproperties=my_font)  # rotation是旋转参数

plt.plot(x, y, color = 'red')
# 添加图形描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度（℃）", fontproperties=my_font)
plt.title("10~12点每分钟气温变化趋势图",fontproperties=my_font)
# plt.savefig("./temperature.png")

# 绘制网格
plt.grid(alpha=0.4)
plt.show()
