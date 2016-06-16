import re, socket
socket.setdefaulttimeout(1)
from urllib import request
url_head = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url_number = '8022'
url = url_head + url_number
data = url
for i in range(400):
    if re.findall(r'[0-9]+', data) == []:
        break
    fails = 0
    print (i, '\n', url, '\n','****')
    while re.findall(r'[0-9]+', data) != []:
        try:
            if fails >= 10: 
                break
            response = request.urlopen(url) 
            data = response.read().decode()
            response.close()
        except:            
            fails += 1
            print ('try　request　again...')
        else:
            break
    print (data + '\n')
    url_number = ''.join(re.findall(r'[0-9]+', data))
    url = url_head + url_number       
    