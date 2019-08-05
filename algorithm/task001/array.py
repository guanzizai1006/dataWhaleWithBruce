"""

"""

class ArrayTask1:

    # 初始化
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    # 取值
    def __getItem__(self, position: int) -> object:
        return self._data[position]

    # 存值
    def __setItem__(self, index: int, value: object):
        self._data[index] = value

    # 数组大小
    def __len__(self) -> int:
        return len(self._data)

    # 生成器输出内容，占用恒定内存大小
    def __iter__(self):
        for item in self._data:
            yield item

    # 查找
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    # 删除
    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    # 加元素
    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    # 输出
    def print_all(self):
        for item in self:
            print(item)


def test_ArrayTask1():

    print("测试文件已运行")

    
    theArray = ArrayTask1(5)

    print("数组长度为： %d"%(len(theArray)))

    theArray.insert(0, 3)
    #theArray.insert(0, 4)
    theArray.insert(1, 5)
    theArray.insert(3, 9)
    theArray.insert(3, 10)
    theArray.delete(0)
    # 5,3,10,9 是输出的内容。
    # 注释掉 insert(0, 4)后 输出5,9,10
     
    print("数组长度为： %d"%(len(theArray)))

    theArray.print_all()


if __name__ == "__main__":
    test_ArrayTask1()




