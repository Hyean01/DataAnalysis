#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import pandas as pd
import numpy as np

# 数据类型Series， 类似一个column
s = pd.Series(np.random.randn(5), name="hyean learn python")  # np.random.randn()函数随机返回一个或者一组样本，具有标准正态分布
print(s)
# Series乘以10
print(f"Series乘以10：\n{s*10}")
# Series取绝对值 adb()函数
print(f"Series取绝对值：\n{abs(s)}")
# 对Series做描述性统计:数值个数、平均值、标准差、最小值、25%、50%、75%、最大值
print(f"Series做描述性统计：\n{s.describe()}")
# 对Series自定义索引
s.index=['hyean', 'qin', "learn", "python", "now"]
print(f"Series自定义索引：\n{s}")
# 对Series做查询---类似字典，索引就是key值
print(f"根据索引查询Series某个值， 索引为learn对应的值为：{s['learn']}")
# 修改Series中某个索引对应的值
s['qin'] = 100
print(f"修改索引对应的值, 修改后的Series为：\n{s}")
# 判断某个索引是否在Series中
print(f"判断某个索引是否在Series中，Hyean是不是Series的索引：{'Hyean' in s}, python是不是Series的索引：{'python' in s}")

# 数据类型DataFrame--- 多个Series的集合
# 读入数据
df = pd.read_excel('GDP.xlsx')
print(type(df), '\n', df)
# 获取指定行/列数据
print(f"获取前5行数据：\n{df.head(5)}")
print(f"获取第3-4行数据：\n{df[2:4]}")
print(f"获取前5行指定列的数据：\n{df[['province', '2018_gdp']].head(5)}")
# 使用整数选择行和列 --- iloc()属性
print(f"使用整数选择行和列(前3行+前4列)：\n{df.iloc[0:3, 0:4]}")
# 重置索引为province  --- 重置为索引的值必须是某个列名， 不然会raise KeyError
df = df[["province", "2010_gdp", "2019_gdp"]]  # 只获取三列
df = df.set_index('province')
print(f"重置索引为province后：\n{df.head(5)}")
# 更改列名
df.columns = ["2010", "2019"]   # 数量要与原dataframe的列对应上
print(f"重置列名后：\n{df.head(5)}")
# 对数据进行计算
df['2010'] = df['2010']/1e4
df['2019'] = df['2019']/1e4
df["increase"] = (df['2019'] - df['2010']) / df['2010']
print(df.head(5))