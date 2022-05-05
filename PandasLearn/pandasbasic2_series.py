#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import numpy as np
import pandas as pd
import random

# 使用列表创建Series
list1 = [1,2,3,4]
s1 = pd.Series(list1)
# 使用字典创建---key就是索引
name = {"ha":323, "hb":332}
s2 = pd.Series(name)
# 使用标量创建
s3 = pd.Series("Test", index=range(4))
# 使用随机数创建
s4 = pd.Series(random.sample(range(100), 9))
print(s4)
# 查看Series的大小
print(s1.shape, s2.shape)
# 命名一个Series
s5 = pd.Series([22,3,12,5,34], name="命名测试")
print(f"命名测试：\n{s5}")
# 通过索引和切片提取Series元素
s6 = pd.Series([22,3,12,5,34,55,67,35,13,14,76], name="Series元素提取测试")
print(f"通过索引和切片提取Series元素：{s6[0]},\n{s6[1:5]}")
# 通过比较提取Series元素
print(s6, "\n", "-"*30)
print(f"通过比较提取Series元素：\n{s6[s6>50]}")
# 通过列表索引提取Series元素 -- 跟索引一样
print(f"通过列表索引提取Series元素：\n{s6[[1,3]]}")
# 通过函数提取Series元素
print(f"通过函数提取Series元素：求平方后的Series值\n{pow(s6, 2)}")
# 通过索引标签提取Series的值--跟索引一样
# 通过in检查Series是否包含特定标签
print(f"通过in检查Series是否包含特定标签：\nis 'j' in s6: {'j' in s6}")

