import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from datetime import datetime
import urllib.request as ur
from numpy.random import randint
import urllib

from config import origin, new

def write_txt_to_file(string ,leixin):
    now = datetime.now()
    r = randint(1000)
    dt_name = str(now.day)+str(now.hour)+str(now.minute)+str(now.second) + str(r)

    with open(os.path.join(BASE_DIR, leixin) + "//"+ dt_name +"."+leixin, "w+") as f:
        f.writelines(string)
        f.close()

    print("写入"+leixin+"文件"+dt_name+"."+leixin)
    return 

from config import INIT_URL
def write_file(url1, leixin):

    if len(url1.split("\\"))>1:
        url = "https:" + url1
    else:
        url = INIT_URL + str(url1)
    print(url)

    headers = {
        'Host':"open.taobao.com",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    req = ur.Request(url=url, headers=headers)
    data = None
    try:
        response = ur.urlopen(req)
        data = response.read()
    except urllib.error.URLError:
        pass
    file_sl = url.split("/")
    f_name = file_sl[len(file_sl)-1]

    with open(os.path.join(BASE_DIR, leixin) +"\\"+ str(f_name), "wb") as f:
        f.write(data)
        f.close()

    print("写入"+leixin+"文件"+f_name)

    origin.append(url1)
    new.append(leixin + "/" + f_name)

    return 

def get_origin_new():
    res = []
    for i in range(len(origin)):
        temp_dict = {}
        temp_dict.setdefault("origin", origin[i])
        temp_dict.setdefault("new", new[i])
        res.append(temp_dict)
    return res

'''
1, 加载保存和替换; 表头全部写上。img为原始和替换

'''