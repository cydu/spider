import random
import urllib
import time
import sys

count = int(sys.argv[1])
for i in xrange(0, count):
    url = "http://beijing.homelink.com.cn/validreg.php?" + (str)(random.random())
    print url
    urllib.urlretrieve(url, sys.argv[2] + "/" + (str)(i) + ".jpg")
    time.sleep(1)
