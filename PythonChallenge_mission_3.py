import re
f = open('one small letter for mission3.txt','r')
lines = f.read()
# print (lines)
f.close()
# res = r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
res = r'[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]'
m = re.findall(res, lines)
print (''.join(m))