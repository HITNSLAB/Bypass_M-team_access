#encoding = utf-8
"""

@Author: c0d3r1iu
@Email: admin@recorday.cn
@File: levelup.py
@Time: 2018/9/22 14:12
"""
import requests
import sys
import time
User_cookie = sys.argv[1]
header={
'Host': 'tp.m-team.cc',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept':'*/*',
'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'https://tp.m-team.cc/index.php',
'Cookie': 'tp='+ User_cookie,
'Connection': 'close'
}
def vote(t):
    print(
    '''
_)+++++++++++++++++++++++++++++++++++++++++++++++++++++++++(_
+      The script is going to up level,Please wait!         +
+                                                           +
+                 Author: C0d3r1iu                          +
+                 Email: admin@recorday.cn                  +
+                                                           +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ''')
    bar = ''
    times = 0
    for i in range(50,51):
        url = 'https://tp.m-team.cc/fun.php?action=vote&id={0}&yourvote=fun'.format(i)
        requests.get(url,headers=header)
        flag = str(int(i / t * 100))
        if int(flag)%10 == 0:
            times+=1
            if times == 9:
                times = 0
                bar += '#####'
        sys.stdout.write('['+flag+'%]'+ bar + '>\r')
        time.sleep(0.01)
        sys.stdout.flush()
    print('Wait to get enough Uploaded')
    time.sleep(0.5)
    upload()


def upload():
    pass
if __name__ == "__main__":
    if(len(sys.argv)==2):
        vote(1046)
        upload()
    else:
        print('[+]  Usage: levelup.py yourcookie')