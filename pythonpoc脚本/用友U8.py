from requests.models import Response as Response
from SpiderMan import *
urls=data_deal("/root/zichan/用友U8.csv")

results=thread_pool(urls,10,'get',payload="/hrss/dorado/console.loadRes.d?res=test")

        