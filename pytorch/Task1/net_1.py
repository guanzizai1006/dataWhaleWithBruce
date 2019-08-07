# test1
# @author: Bruce
# @time:   20190806
# @aims:   输出网络的内容，包括卷积层、全连接层

import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        # nn.Module 子类的函数必须在构造函数中执行父类的构造函数
        # 下式等价于 nn.Module.__init__(self)
        # super(Net, self).__init_()
        super(Net, self). __init__()


        # 卷积层'1'表示输入图片为单通道，
        # '6'表示输出通道数
        # '5'表示卷积核为5*5
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        
        # 全连接层
        self.fc1  = nn.Linear(16*5*5, 120)
        self.fc2  = nn.Linear(120, 84)
        self.fc3  = nn.Linear(84, 10)

    def forward(self, x):
        # 卷积 -> 激活 -> 池化
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # reshape
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()

print(net)
print("\n")

params = list(net.parameters())
print(len(params))

print("\n")
for name,parameters in net.named_parameters():
    print(name, ':', parameters.size())




