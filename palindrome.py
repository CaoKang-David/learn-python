''' 生成回数 （指从左至右读与从右向左读是一样的，如12321 909）'''
## def is_palindrome(n) 判断是否回数 传入int型数字
## 如果是回数 返回True, 否则 返回False

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
# test the def function
# output = filter(is_palindrome, range(1,1000))
# print (list(output))