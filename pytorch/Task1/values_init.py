from __future__ import print_function
import torch as t

print("Bruce的 torch 版本为： %s"%(t.__version__))
print("\n\n\n")

# 构建 5*3 矩阵，分配空间，未初始化
x = t.Tensor(5, 3)
x_1 = t.Tensor([[1,2], [3, 4]])


print("输出x的内容，为5行3列")
print(x)
print("\n")
print("输出y的内容，两行两列，元素为 1,2,3,4")
print(x_1)
print("\n")
print("输出x的形状")
print(x.size())
print("\n")
print("输出x的列数,2种写法")
print(x.size()[1])
print(x.size(1))





