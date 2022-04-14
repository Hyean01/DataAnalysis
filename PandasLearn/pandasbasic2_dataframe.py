#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import numpy as np
import pandas as pd

# 手动创建DataFrame
data1 = {'姓名': ['陈芳', '李斯', '公孙龙', '莫容', '秦琴', '宁凝', '莉莉', '慕容清', '诸葛与', '白羽莫'],
        '年龄': [12, 18, 19, 22, 22, 30, 50, 55, 61, 88],
        '爱好': ['羽毛球', '足球', '足球', '排球', '跑步', '徒步', '游泳', '探险', '读书', '下棋']}
df = pd.DataFrame(data1)
print(df)
#将外部文件读取到DataFrame
data2 = pd.read_csv('food.csv', encoding='ISO8859-1')
# ISO08859-1属于单字节编码，最多能表示的字符范围是0-255，应用于英文系列
print(type(data2))
# 查看DataFrame的大小
print(f"DataFrame的大小：{data2.shape}")
# 预览DataFrame
print(f"查看DataFrame的前5行：\n{data2.head(5)}")
print(f"查看DataFrame的后5行：\n{data2.tail(5)}")
# 查看所有列、指定列的数据类型
print(f"查看DataFrame所有列的数据类型：\n{data2.dtypes}")
print(f"查看DataFrame指定列的数据类型：\n{data2['Item Code'].dtypes}")
# 更改列的数据类型
data3 = data2['Item Code'].astype(str)
print(f"更改指定列的数据类型后：\n{data3.dtypes}")
# 数字列的描述性统计
print(f"数字列的描述性统计：\n{data2['Y2013'].describe()}")
# 字符串列的描述性统计
print(f"字符串列的描述性统计：\n{data2['Area'].describe()}")
# 对整个DataFrame进行描述性统计 --- 只对数字列进行描述性统计
print(f"整个DataFrame的描述性统计：\n{data2.describe()}")
# 选择列
print(f"使用点符号选择列：\n{data2.Item.head()}")
print(f"使用方括号选择列：\n{data2['Element'].head()}")
print(f"使用数字索引和iloc选择器选择列：\n{data2.iloc[:,4]}")  # 4--第4列
# 选择多列
print(f"通过列名选择多列：\n{data2[['Area', 'Y2013']].tail()}")
print(f"使用数字索引和iloc选择器选择多列：\n{data2.iloc[:,4:10].head()}")  # 4-10列
print(f"使用数字索引和iloc选择器选择多行：\n{data2.iloc[1:10,:].head()}")  # 1-10行
# 使用loc选择器进行基于标签的行选择
print(f"使用loc选择器进行基于标签的行选择：\n{data2.loc[2,:]}")  # 列出第2行的所有数据
# 基于逻辑判断选择多行
print(f"基于逻辑判断选择多行：\n{data2[data2['Item'] == 'Barley and products'].head()}")  # 列出Item==Barley and products 的前5行数据
# 选择求和、平均数、中位数
print(f"求和、平均值、中位数、最大值、最小值：{data2['Y2013'].sum(), data2['Y2013'].mean(), data2['Y2013'].median(), data2['Y2013'].max(), data2['Y2013'].min()}")
# 删除
# 删除一列
data4 = data2.drop('Area', axis=1)  # 是data4少了Area列，但是data2还有Area列
data5 = data2.drop(columns='Item')  # 是data5少了Item列，但是data2还有Item列
print(f"删除Area列后：\n{data4.head()}")
print(f"删除Item列后：\n{data5.head()}")
# 删除多列
data6 = data2.drop(['Area', 'Item', 'Item Code'], axis=1)
print(f"删除多列后：\n{data6.head()}")
# 删除行 -- 根据数据标签而不是索引
data7 = data2.drop([1, 5],axis=0)  # 删除第2、6行
print(f"删除第2、6行后：\n{data7.head()}")
# 重命名列
data8 = data2.rename(columns={'Item':'Items'})
print(f'把Item列重命名为Items：\n{data8.head()}')
# 将所有列名转为小写
data9 = data2.rename(columns=lambda x: x.lower())
print(f'把所有列名转为小写：\n{data9.head()}')
# 保存和导出DataFrame
# data9.to_csv('new_food.csv', index=False, encoding='utf8')
# data9.to_excel('new_food.xlsx', index=False, encoding='utf8')

# 使用matplotlib画直方图
import matplotlib.pyplot as plt
