"""
合并有序数组
要求时间复杂度
"""

def mergeArray(aList, bList):
    reslut = []
    lenAList = len(aList)
    lenBList = len(bList)

    i = 0
    j = 0

    while i < lenAList and j < lenBList:
        if aList[i] <= bList[j]:
            reslut.append(aList[i])
            i += 1
        else:
            reslut.append(bList[j])
            j += 1

    if i < lenAList:
        reslut.extend(aList[i:])
    if j < lenBList:
        reslut.extend(bList[j:])

    return reslut

a = [1,3,5,7,9]
b = [2,4,6,8,10]
print(mergeArray(a, b))



