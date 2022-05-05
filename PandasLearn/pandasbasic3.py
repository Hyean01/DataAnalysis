#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import pandas as pd
import numpy as np
import random

# 先获取数据
df = pd.read_csv(r"uk.csv")
# 添加随机数字列id
df['id'] = [random.randint(1,1000) for x in range(df.shape[0])]
print(df)

# 通过iloc选择单行或者单列
print(f"通过iloc选择第一行：\n{df.iloc[0]}")
print(f"通过iloc选择第一列：\n{df.iloc[:,0]}")
print(f"通过iloc选择最后一行：\n{df.iloc[-1]}")
print(f"通过iloc选择最后一列：\n{df.iloc[:,-1]}")
print(f"通过iloc选择多行：\n{df.iloc[1:4]}")
print(f"通过iloc选择多列：\n{df.iloc[:,-4:-1]}")
print(f"通过iloc选择第1行、第三行、第2列、第4列的数据：\n{df.iloc[[0,2],[1,3]]}")
print(f"通过iloc选择第1-3行，2-4列的数据：\n{df.iloc[0:3, 1:4]}")
