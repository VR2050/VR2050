import requests  
from concurrent.futures import ThreadPoolExecutor, as_completed  
import pandas as pd 

def data_deal(file_path:str):
    df=pd.read_csv(file_path)
    return df["link"].tolist()



class Scan_base:  
    def __init__(self, response: requests.Response, url: str) -> None:  
        self.response = response  
        self.url = url  
  
    def scans(self):  
        if self.response and self.response.status_code == 200:  
            return self.url + " 存在漏洞"  
        
        return "hello world"
  
class Scan_bykeys(Scan_base):  
    def scans(self, keys: str):  
        if self.response and self.response.text.find(keys) != -1:  
            return self.url + " 存在漏洞"  
        return None  
  
headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'  
}  
  
def spider_get(url: str, headers: dict):  
    try:  
        r = requests.get(url, headers=headers, timeout=5)  
        return r, url  
    except:  
        #print(f'{url}请求失败')  
        return None, url  
  
def spider_post(url: str, headers: dict, data: dict):  
    try:  
        r = requests.post(url, headers=headers, data=data, timeout=5)  
        return r, url  
    except:  
        # print(f'{url}请求失败')  
        return None, url  
  
def thread_pool(urls: list, thread_num: int, method: str, data: dict=None, keys: str = None,payload:str=None):  
    results = []  
    with ThreadPoolExecutor(max_workers=thread_num) as executor:  
        if method == 'get':  
            futures = [executor.submit(spider_get, url+payload, headers) for url in urls]  
        elif method == 'post':  
            futures = [executor.submit(spider_post, url+payload, headers, data) for url in urls]  
        for future in as_completed(futures):  
            response, url = future.result()  
            if response:  
                if keys:  
                    scan = Scan_bykeys(response, url)  
                    scan_result = scan.scans(keys)  
                else:  
                    scan = Scan_base(response, url)  
                    scan_result = scan.scans()  
                if scan_result:  
                    results.append(scan_result)  
                    print(scan_result)  
            else:  
                print(f"No response for {url}")  
    return results  
  
def save_results(results: list, file_name: str):  
    with open(file_name, 'w') as f:  
        for result in results:  
            f.write(result + '\n')  
  
