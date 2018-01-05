# coding=utf-8
import numpy as np


# 定义神经网络结构
class Network(object):
    def __init__(self, sizes):
        # 网络层数
        self.num_layers = len(sizes)
        # 每层神经元的个数
        self.sizes = sizes
        # 初始化每层的偏置
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        # 初始化每层的权重
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]


#sigmoid激励函数
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 创建网络
net = Network([3,2,1])
net = Network([3, 2, 1])
print net.num_layers
print net.sizes
print net.biases
print net.weights

