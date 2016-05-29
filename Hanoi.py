def Hanoi(n, source, bridge, target):           # n为盘子数；source为起点柱子， bridge为中转柱子，target为目标柱子
    if n==1:
        print ('%s --> %s' % (source, target))  # 如果只有一个盘子，则将盘子从起点直接搬至终点
    else:                                       # 如果盘子不止一个 则按如下步骤搬动盘子
        Hanoi(n-1, source, target, bridge)      # 如果不止一个盘子，则先要将n-1个盘子 借助目标柱子 搬至中转柱子
        Hanoi(1, source, bridge, target)        # 将剩余的最后一个盘子直接搬至目标柱子
        Hanoi(n-1, bridge, source, target)      # 最后将前n-1个盘子 从中转柱子 借助起点柱子 搬至目标柱子

##测试示例：
##print ('******************')
##Hanoi (1,'A','B','C')
##print ('******************')
##Hanoi (2,'A','B','C')
##print ('******************')
##Hanoi (3,'A','B','C')
##print ('******************')
##Hanoi (4,'A','B','C')

