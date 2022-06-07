import re

from time import sleep
from idna import alabel
import requests
from bs4 import BeautifulSoup
from functions import download_images, get_filename_include_extension,get_image_extension
from os.path  import basename
sample_url = 'https://www.coupang.com/vp/products/171659469?vendorItemId=4241702026&isAddedCart='
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'referer' : 'https://www.coupang.com/np/products/brand-shop?brandName=%EC%93%B0%EC%9E%84',
    }

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import UnexpectedAlertPresentException, TimeoutException
    
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    
    driver = webdriver.Chrome(options=options)
    driver.get(sample_url)
    try:
        element = WebDriverWait(driver, 20).until(
            # 아래 element가 발견되면 로딩이 성공적인것
            EC.presence_of_element_located((By.XPATH, '//li[@class="product-detail"]/div/div'))
        )
    except UnexpectedAlertPresentException as e:
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        alert.dismiss()
        print(e)
    except TimeoutException as e:
        print(e)
    finally:
        pass
    elements = driver.find_elements(by=By.XPATH, value='//img')
    src_set = set()
    for element in elements:
        src = element.get_attribute('src')
        if len(get_image_extension(src)) > 0:
            src_set.add(src)
    for src in src_set:
        download_images(src=src, path='images\\',filename=get_filename_include_extension(url=src))

        