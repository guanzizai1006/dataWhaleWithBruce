# pytorch 完成线性回归

import torch as t
import numpy as np
from matplotlib import pyplot as plt

# 线性回归
# y = 2 * x + 1
# 生成数据，添加噪音，使不完全拟合上式
X = np.random.rand(100)*10 
# 100个随机数乘以10,使得范围在(0,10)
Y = 2 * X + 1 + np.random.rand(100)

# print(X, Y)
plt.scatter(X, Y)
# plt.show() # Bruce，一定要加上show()，才可以显示的哦

# 随即初始化参数
w = t.rand(1, 1, requires_grad = True)
b = t.rand(1, 1, requires_grad = True)

def model_LR(X, Y, w, b, lr, iters):
    x = t.Tensor(X).reshape([-1, 1])
    y = t.Tensor(Y).reshape([-1, 1])
    losses = np.zeros(iters)
    for i in range(iters):
        # forward: 计算loss
        y_pred = x.mm(w) + b.expand_as(y)
        loss = 0.5 * (y_pred - y) ** 2
        loss = loss.mean()
        losses[i] = loss.item()

        # backward: 手动计算梯度
        loss.backward()

        # 更新参数
        w.data.sub_(lr * w.grad.data)
        b.data.sub_(lr * b.grad.data)

        # 梯度清零
        w.grad.data.zero_()
        b.grad.data.zero_()

    print(w)
    print

    print(b)
    return w, b
model_LR(X,Y,w,b,0.01, 5000)

'''
# 画出生成的函数
x_out = np.linspace(0, 10, 100)
print(x_out.shape)
# y_out = w * x_out + b
y_out = np.dot(w,x_out)# + b
plt.scatter(x_out, y_out)
plt.show()
'''


print("pytorch 的 线性回归测试完毕")
