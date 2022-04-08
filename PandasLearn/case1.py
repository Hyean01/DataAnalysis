#!/usr/bin/env python 
# -- coding:utf-8 -- 
# hyean.qin@gmail.com
import pandas as pd
import numpy as np
persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(persons)
print(df.loc[3,"age"])
print(df.to_string())