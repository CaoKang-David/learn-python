# def mission_2(string):
   # return chr(ord(string) + 2)

test = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. 
rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. 
lmu ynnjw ml rfc spj.'''
# result_text = []
# for i in test:
    # if i <= 'x' and i >= 'a':
        # result_text.append(mission_2(i))
    # elif i == 'y':
        # result_text.append('a')
    # elif i == 'z':
        # result_text.append('b')
    # else:
        # result_text.append(i)
# result_text = ''.join(result_text)    
# print (result_text)
intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
transtab = test.maketrans(intab, outtab)
print (test.translate(transtab))