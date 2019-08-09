'''
@goals :  numpy 和 pytorch 实现梯度下降法
@time  :  20190809
@author:  Bruce

@梯度下降法的一般步骤：
- 设定初始值
- 求梯度
- 在梯度方向上完成参数的更新

'''

# 2. 然后是pyTorch版本的梯度下降
#    拟合 y = 2*x1 - 4*x2, 2元线性函数，x是2维向量
#    梯度下降法来求解最优参数

import torch
from torch.autograd import Variable
import numpy as np

N = 100
x = Variable(torch.randn(N, 2))
w = Variable(torch.FloatTensor([2, -4]))
y = x*w

EPOCHS = 5000

lr    = 0.01
w_GD  = Variable(torch.FloatTensor([0, 0]), requires_grad = True)
cost  = []
w_all = []
for i in range(EPOCHS):
    w_all.append(w_GD.data)
    y_predict = x*w_GD
    loss = torch.mean((y_predict - y)**2)

    cost.append(loss.data.numpy())
    loss.backward()
    # 参数更新
    w_GD.data -= lr*w_GD.grad.data
    w_GD.grad.data.zero_()
print("loss: ", loss)
print("w_GD: ", w_GD)

print("完成梯度下降测试")



