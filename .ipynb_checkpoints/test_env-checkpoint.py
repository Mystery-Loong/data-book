import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression

print("所有库导入成功！")
print("NumPy版本:", np.__version__)
print("Pandas版本:", pd.__version__)

# 创建一个简单的图并保存
plt.plot([1, 2, 3, 4])
plt.ylabel('一些数字')
plt.savefig('test_plot.png')
print("基本绘图功能测试成功！ 图片已保存为'test_plot.png'")
