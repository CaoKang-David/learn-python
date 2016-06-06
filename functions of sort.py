''' sorted() 函数的应用'''
## 两个函数 对一组tuple排序 如 L = [('bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
## 按名字排序 从小到大
## 按成绩排序 从大到小

L = [('bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
print (sorted(L, key = lambda L: str.lower(L[0])))
print (sorted(L, key = lambda L: L[1], reverse = True))
