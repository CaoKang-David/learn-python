from urllib import request
response = request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

import pickle
data = pickle.load(response)
response.close()
for line in data:  
    print (''.join(t[0] * t[1] for t in line))
