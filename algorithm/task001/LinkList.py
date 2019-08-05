# coding=utf-8


class SingleNode:

    def __init__(self, value, next_data=None):
        self.data = value
        self.next = next_data

class DoubleNode:

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.data = value
        self.next = next


class LinkList:

    def __init__(self, data, double_link=False, loop=False):
        self.header = None
        if double_link:
            self.double = True
            if data:
                if not loop:
                    self.header = DoubleNode(data[0])
                    link = self.header
                    for i in data[1:]:
                        node = DoubleNode(i, link)
                        link.next = node
                        link = link.next
                else:
                    pass
                    # 由于时间有限，这里可能会出问题，还没来得及检测，建议直接pass
  

            else:
                raise IOError("Init error")
        else:
            self.double = False
            if data:
                if not loop:
                    self.header = SingleNode(data[0])
                    link = self.header
                    for i in data[1:]:
                        node = SingleNode(i)
                        link.next = node
                        link = link.next
                else:
                    pass
                    # 单链表循环链表，有待测试

            else:
                raise IOError("Init error")

    def length(self):
        index = 0
        link = self.header
        while link.next:
            index += 1
            link = link.next
        index += 1
        return index

    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def insert(self, index, value):
        if not self.double:
            if self.is_empty():
                if index < 0 or index > self.length():
                    raise IndexError("Link list is empty")
                elif index == 0:
                    self.header = SingleNode(value)
            else:
                link = self.header
                link_new = SingleNode(value)
                index_num = 0
                while link.next:
                    if index_num == index - 1:
                        link_new.next = link.next
                        link.next = link_new
                        break
                    else:
                        index_num += 1
                        link = link.next
        else:
            if self.is_empty():
                if index < 0 or index > self.length():
                    raise IndexError("Link list is empty")
                elif index == 0:
                    self.header = DoubleNode(value)
            else:
                link = self.header
                link_new = DoubleNode(value)
                index_num = 0
                while link.next:
                    if index_num == index - 1:
                        link_new.next = link.next
                        link.next.prev = link_new
                        link_new.prev = link
                        link.next = link_new
                        break
                    else:
                        index_num += 1
                        link = link.next

    def append(self, value):
        if not self.double:
            if isinstance(value, SingleNode):
                node = value
            else:
                node = SingleNode(value)
            if not self.header == None:
                link = self.header
                while link.next:
                    link = link.next
                link.next = node
            else:
                self.header = node
        else:
            if isinstance(value, SingleNode):
                node = value
            else:
                node = DoubleNode(value)
            if not self.header == None:
                link = self.header
                while link.next:
                    link = link.next
                link.next = node
                node.prev = link
            else:
                self.header = node

    def delete(self, index):
        if not self.double:
            link = self.header
            index_num = 0
            while link.next:
                if index_num == index:
                    link.next = link.next.next
                    break
                else:
                    index_num += 1
        else:
            link = self.header
            index_num = 0
            while link.next:
                if index_num == index:
                    link.next = link.next.next
                    link.next.next.prev = link
                    break
                else:
                    index_num += 1


    def get_index(self, value):
        if self.is_empty():
            raise IndexError("Link list is empty")
        link = self.header
        index = 0
        while link:
            if index < self.length():
                if link.data == value:
                    return index
                else:
                    link = link.next
                    index += 1
            else:
                raise IndexError("data is not exist")

    def get_item(self, index):
        if self.is_empty():
            raise IndexError("Link list is empty")
        if not isinstance(index, int):
            raise IndexError("Index must be integer")
        if index < 0 or index > self.length():
            raise IndexError("Out of index")
        link = self.header
        index_num = 0
        while link.next:
            if index_num == index:
                return link.data
            else:
                link = link.next
                index_num += 1

    def get_node(self, index):
        if not isinstance(index, int):
            raise IndexError("Index type error")
        link = self.header
        index_num = 0
        while link.next:
            if index_num == index:
                mid_node = link
                return mid_node
            else:
                link = link.next
                index_num += 1

    def reversed(self):
        if not self.double:
            link = self.__reversed_s(self.header)
            self.header = link
        else:
            link = self.__reversed_d(self.header)
            self.header = link

    def __reversed_s(self, node):
        """
        :param node:
        :return:
        """
        if node.next == None:
            return node
        link = self.__reversed_s(node.next)
        node.next.next = node
        node.next = None
        return link

    def __reversed_d(self, node):
        """
        :param node:
        :return:
        """
        if node.next == None:
            return node
        link = self.__reversed_s(node.next)
        node.next.next = node
        node.prev = node.next
        node.next = None
        return link

    def to_list(self):
        if self.is_empty():
            raise IOError("Link list is empty")
        res_list = []
        link = self.header
        while link.next:
            res_list.append(link.data)
            link = link.next
        res_list.append(link.data)
        return res_list

    def get_mid_node(self):
        length = self.length()
        if length % 2 == 0:
            raise IOError("Link list have no middle node")
        else:
            mid_index = length // 2
            middle_node = self.get_node(mid_index)
            return middle_node

if __name__ == '__main__':

    # # 单链表
    # slink = LinkList([1, 2, 3, 4, 5])
    # slink.insert(2, 8)
    # slink.append(5)
    # # slink.delete(2)
    # # print(slink.length())
    # # print(slink.is_empty())
    # # print(slink.get_index(5))
    # # print(slink.get_item(5))
    # print(slink.to_list())
    #
    # # 获取中间节点
    # mid_node = slink.get_mid_node()
    # print(mid_node.data)
    #
    # # 链表反转
    # slink.reversed()
    # # print(slink.get_item(1))
    # print(slink.to_list())
    #
    # # 两个有序链表合并
    # sl1 = LinkList([1, 3, 5, 7, 9])
    # sl2 = LinkList([2, 4, 6, 8, 10])
    # res_list = sl1.to_list() + sl2.to_list()
    # res_list.sort()
    # res_link = LinkList(res_list)
    # print(res_link.to_list())

    # 双链表
    slink = LinkList([1, 2, 3, 4, 5], double_link=True)
    slink.insert(2, 8)
    slink.append(5)
    # slink.delete(2)
    # print(slink.length())
    # print(slink.is_empty())
    # print(slink.get_index(5))
    # print(slink.get_item(5))
    print(slink.to_list())

    # 获取中间节点
    mid_node = slink.get_mid_node()
    print(mid_node.data)
    print(mid_node.prev.data)

    # 链表反转
    slink.reversed()
    # print(slink.get_item(1))
    print(slink.to_list())

    # 两个有序链表合并
    sl1 = LinkList([1, 3, 5, 7, 9])
    sl2 = LinkList([2, 4, 6, 8, 10])
    res_list = sl1.to_list() + sl2.to_list()
    res_list.sort()
    res_link = LinkList(res_list)
    print(res_link.to_list())

