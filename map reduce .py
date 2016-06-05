''' 高阶函数练习题：'''

## normalize()  send string to the def function 
## input normalize(strname)  i.e. 'adam'
## output 'Adam'
## use map function to output a list of string processed by normalize
from functools import reduce
def normalize(name):
    return name.title()

# test the def function
# L1 = ['adam', 'Lisa', 'barT'] 
# L2 = list(map (normalize, L1))
# print (L2)


## prod() input a list of number 
## output the multiplized number in the list
## use reduce function to output 

def prod(L):
    return reduce(lambda x, y: x * y, L)

# test the def function

# print ('3 * 5 * 7 * 9 = ', prod([3,5,7,9]))

## str2float() input a string like '123.456' as an argument
## output a float number like 123.456
## use the higher order function like map and reduce

def str2float(s):
    index = s.index('.')
    def char2num(char):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[char]
    number_before_point = reduce(lambda x, y: x * 10 + y, map(char2num, s[:index]))
    number_after_point = reduce(lambda x, y: x / 10.0 + y, map(char2num, s[:index:-1]))/10
    return number_before_point + number_after_point

# test the def function 
# print ('str2float(\'123.456\') =', str2float('123.456'))
    
    
    
    
    
    
    
    
    
    
    
    

    
    