#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import numpy as np

# 数据类型---数组里具体元素的数据类型
j = np.arange(3, dtype=float)
print(j, j.dtype, type(j))
# 数据类型转换---不会改变原来数组元素的数据类型，是新生成了一组数组，需要用新的变量去指向它
g = j.astype(float)
print(g, g.dtype)
print(id(j), id(g))
# 数组创建
# 方法一：将列表 或者 元组传入np.array（）来创建
print(np.array([1, 2, 3]), np.array((1, 2, 2, 3, 4)))
# 方法二：初始化数组的值，只需要传入元素的个数即可
print(np.zeros(3), np.ones(4), np.random.random(3), np.random.randint(1, 7, size=8))
# 数组运算
array1 = np.array([1, 4, 7])
array2 = np.random.randint(2, 10, size=3)
print(array1, array2)
# 数组间的加减乘除、与单个值的计算
jia = array1 + array2
jian = array2 - array1
cheng = array1 * array2
chu = array1 / array2
shuzhi1 = array1 * 100
shuzhi2 = array2 / 5
print(f"数组的加减乘除以及与单个数值的计算", jia, jian, cheng, chu, shuzhi1, shuzhi2)
# 数组切片 --- 与列表操作一致
array3 = np.random.randint(1, 15, size=10)
print(f"数组的切片：", array3, array3[0], array3[3:4], array3[:7], array3[5:])
# 聚合函数
array4 = np.array([1, 1, 3, 5, 7, 8, 9, 11, 2, 4, 5, 23, 12, 67, 23, 111, 88, 97, 56, 47, 89, 34, 0])
print(f'聚合函数：最大值：{array4.max()},最小值：{array4.min()},均值：{array4.mean():.2f}， 求和：{array4.sum()},标准差：{array4.std():.3f}')

# 矩阵操作
# 创建矩阵
# 方法一：通过将二维列表传给Numpy来创建矩阵
print(np.array([[1, 2], [5, 7]]))  # 注意，是把两个列表放在一个列表或者元组里传参给array
print(np.array(([1, 4, 7], [2, 5, 8])))
# 方法二：传入一个元组来描述矩阵维度
print(np.zeros((2, 3)))
print(np.ones((3, 3)))
print(np.random.random((4, 5)))
print(np.random.randint(4, 55, size=(3, 5)))
# 矩阵运算
# 相同大小矩阵的加减乘除
juzhen1 = np.array([[2, 4, 7], [11, 45, 87]])
juzhen2 = np.random.randint(8, 20, (2, 3))
print(juzhen1, juzhen2)
# 加减乘除
jia1 = juzhen1 + juzhen2
jian1 = juzhen2 - juzhen1
cheng1 = juzhen1 * 10  # 数乘
# chu1 = juzhen1 / juzhen2
print(f"矩阵的加：\n {jia1}, \n矩阵的减：\n {jian1}, \n矩阵的数乘：\n {cheng1}")
# 不同大小的矩阵的加减乘除， 仅两个矩阵的秩数为1时

# 矩阵的切片 ---在不同维度上使用索引操作来对数据进行切片
juzhen3 = np.array([[1, 3], [5, 8], [9, 4]])
print(juzhen3)
print(f"第1行第2列的数据: {juzhen3[0, 1]}")  # 第1行第2列的数据
print(f"第2-3行: \n {juzhen3[1:3]}")  # 第2-3行
print(f"第1-2行， 第1列: \n {juzhen3[0:2, 0]}")  # 第1-2行， 第1列
# 聚合矩阵
print(f"最大值：{juzhen3.max()}， 最小值：{juzhen3.min()}， 求和：{juzhen3.sum()}, 平均值：{juzhen3.mean()}, 标准差:{juzhen3.std()}")
# 使用axis参数指定行和列进行聚合
print(f"纵向求最大值： {juzhen3.max(axis=0)}, 横向求平均值：{juzhen3.mean(axis=1)}")

# 矩阵的重置
juzhen4 = np.array([[1, 3, 5], [2, 7, 8], [4, 5, 9]])
print(f"矩阵转置前：\n {juzhen4}, \n矩阵转置后：\n {juzhen4.T}")
# reshape()方法改变某个矩阵的维度
juzhen5 = np.array([1, 3, 5, 7, 9, 11])
print(f"重构成一个A23的矩阵：\n {juzhen5.reshape(2, 3)}, \n重构成一个A32的矩阵：\n {juzhen5.reshape(3, 2)}")
