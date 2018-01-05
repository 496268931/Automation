#coding=utf-8
import numpy as np

a = np.array([2,3,4])

print a
#表示数组中元素类型的选项，可使用标准的python类型穿件或指定dtype。也可使用NumPy提供的数据类型
print a.dtype
#数组的维度。例如二维数组中，表示数组的行数和列数
print a.shape
#数组的维数，二维数组（矩阵）
print a.ndim
#数组元素的总个数，等于shape属性中元组元素的乘积
print a.size

b = np.array([[1,2],[3,4]])
print b
b2 = np.array([[1,2],[3,4]],dtype = float)
print b2
b3 = np.zeros((3,4))
print b3
b4 = np.ones((3,4))
print b4
b5 = np.ones((2,3))
print b5
print b5.reshape((3,2))

print
c = np.ones((3,4))
d = c*2
print c
print d
print np.hstack((c,d))
print np.vstack((c,d))