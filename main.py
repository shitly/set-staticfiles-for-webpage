# _*_ coding:utf-8 _*_
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

def set_static():
    for file in ["css", "img", "js"]:
        try:
            os.makedirs(os.path.join(BASE_DIR, file))
        except FileExistsError:
            pass 

set_static()


from config import URL, INIT_URL
import urllib.request as ur
from bs4 import BeautifulSoup


class Spyder():
    def __init__(self, url):
        self.url = url

    def open_url(self):
        url = self.url
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        req = ur.Request(url=url, headers=headers)
        response = ur.urlopen(req)
        return response.read().decode('utf-8')
    
    def __str__(self):
        return self.open_url()

import re
def link_to_main(link):
    partern = '''.*<link .*?href="(.*?)".*'''
    return re.findall(partern, repr(link))   

def script_to_main(script):
    partern = '''<script.*?src="(.*?)"></script>'''
    return re.findall(partern, repr(script))  

def img_to_main(img):
    partern = '''.*<img.*?src="(.*?)".*>.*'''
    return re.findall(partern, repr(img))  


from tools import write_file, write_txt_to_file


def extract_static_to_data():
    url = URL

    data = Spyder(url).open_url()
    # 先写 index.html
    with open(BASE_DIR + "//"+ "index.html", "w+") as f:
        f.writelines(data)
        f.close()

    soup1 = BeautifulSoup(data, 'html.parser')
    csss = soup1.findAll("link")
    scripts = soup1.findAll("script")
    imgs = soup1.findAll("img")
   
    for x in scripts:
        if len(script_to_main(x)) < 1:
            # 直接写整个文本进一个随机js文件
            write_txt_to_file(x, "js")
        else:
            # 二进制形式写入一个js文件
            write_file(script_to_main(x)[0], "js")

    for x in imgs:
        write_file(img_to_main(x)[0], "img")
    
    for x in csss:
        write_file(link_to_main(x)[0], "css")
    return 

extract_static_to_data()    


