f = open('rare character for mission2.txt')
lines = f.readlines()
string = ''
for line in lines:
    for i in line:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            string += i
print (''.join(string))
