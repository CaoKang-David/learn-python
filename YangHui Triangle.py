def triangles():  # 杨辉三角 生成器法实现
    n = 1  #第n行，从1开始
    line = [1]  # line 输出第n行的结果 初始为第一行的数字
    while True:
        yield line # 生成line
        line_temp = [0] + line + [0] #临时list 在line的基础上，首尾各加一个0， 用于后面列表生成式中直接生成line
        n = n + 1  #进入第n+1行
        line = [line_temp[x] + line_temp[x+1] for x in list(range(n))] #在line_temp的基础上，按照杨辉三角的规则，利用列表生成式直接生成line

# 测试代码示范

##n = 0
##for t in triangles():
##    print(t)
##    n = n + 1
##    if n == 10:
##        break
    
            
