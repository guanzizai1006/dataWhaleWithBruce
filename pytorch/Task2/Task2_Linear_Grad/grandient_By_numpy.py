'''
@goals :  numpy 和 pytorch 实现梯度下降法
@time  :  20190809
@author:  Bruce

@梯度下降法的一般步骤：
- 设定初始值
- 求梯度
- 在梯度方向上完成参数的更新

'''

# 1. 首先是numpy版本的梯度下降
#    拟合 y = 2*x1 - 4*x2, 2元线性函数，x是2维向量
#    梯度下降法来求解最优参数

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style


# 创建数据
N  = 100
x1 = np.linspace(-10, 10, N)
x2 = np.linspace(-15, 5,  N)

x = np.concatenate(([x1], [x2]), axis = 0).T
w = np.array([2, -4])
y = np.dot(x, w)
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

ax1.plot_wireframe(np.array([x1]), np.array([x2]), np.array([y]), rstride = 5, cstride = 5)
ax1.set_xlabel("x1")
ax1.set_ylabel("x2")
ax1.set_zlabel("y")

# 梯度下降
EPOCHS = 50  
LOSS_MIN = 0.0001 # loss的目标最小值，当loss小于这个值时停止迭代
lr = 0.01
w_GD = np.zeros(2)

cost = [] # 梯度下降过程中存储loss的值
w_all = []
for i in range(EPOCHS):
    w_all.append(w_GD.copy())
    y_predict = np.dot(x, w_GD) # 使用当前w_GD的y预测值
    loss = np.mean((y_predict - y)**2) # 计算loss
    cost.append(loss)
    dw = np.mean(2 * (y_predict-y)*x.T, axis = 1) # 计算梯度
    w_GD -= lr*dw # 梯度下降

print("loss: ", loss)
print("W1: ", w_GD[0], "w2:", w_GD[1])

# 画出梯度的下降曲线
w_all = np.array(w_all)
fig = plt.figure()
ax2 = fig.add_subplot(111, projection = '3d')
ax2.plot_wireframe(np.array([w_all[:,0]]), np.array([w_all[:,1]]), np.array([cost]))
ax2.set_xlabel("w1")
ax2.set_ylabel("w2")
ax2.set_zlabel("loss")
fig = plt.figure()

# 画出loss-iteration曲线
plt.plot(range(len(cost)), cost)
plt.title('loss')
plt.xlabel('iteration')
plt.ylabel('loss')
plt.show()








