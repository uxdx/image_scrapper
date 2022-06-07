from fileinput import filename
from pyclbr import Function
from sqlite3 import Time
import time
from tkinter import Image
from typing import List, Tuple
from functions import *
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
sample_url = 'https://www.coupang.com/vp/products/2040637002?itemId=3469208914&vendorItemId=71455552336&isAddedCart='
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'referer' : 'https://www.coupang.com/np/products/brand-shop?brandName=%EC%93%B0%EC%9E%84',
    }

class ImageScrapper:
    """
    링크와 여러가지 옵션을 추가해서 run하면
    이미지 파일들을 반환하는 클래스
    """
    options = Options()
    # options.add_argument('headless')
    def __init__(self, url:str) -> None:
        self.driver = webdriver.Chrome(options=self.options)
        self.load_page(url)
    
    def scrap(self, xpath:str):
        elements = self.find_elements(by=By.XPATH, value=xpath)
        print(len(elements))
        self.save_images(elements)
        
    def load_page(self, url:str):
        self.driver.get(url)
        # body = self.driver.find_element_by_css_selector('body')
        # # 페이지를 밑으로 내려서 더 많이 로드하게 함.
        # for i in range(10):
        #     body.send_keys(Keys.PAGE_DOWN)
        #     print(i)
        #     time.sleep(1)

        
    def find_elements(self, by=By.XPATH, value='//'):
        try:
            elements = WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_elements(by=by,value=value))
        except:
            return []
        return elements

    def save_images(self, elements:List, path='images\\'):
        src_set = set()
        for element in elements:
            src = element.get_attribute('src')
            if len(get_image_extension(src)) > 0:
                src_set.add(src)
        for src in src_set:
            filename = get_filename_include_extension(url=src)
            print("Download image at ", path, filename)
            download_images(src=src, path=path, filename=filename)


if __name__ == '__main__':
    urls = [
        'https://ssueim.com/product/%EB%A7%88%EC%9A%B4%ED%8B%B4-%EC%BA%A0%ED%95%91-%EC%8A%A4%ED%85%90%EB%A8%B8%EA%B7%B8-440ml-2color/6523/category/172/display/1/',
        'https://ssueim.com/product/%EB%A7%88%EC%9A%B4%ED%8B%B4-%EC%8A%A4%ED%85%90-%ED%85%80%EB%B8%94%EB%9F%AC-500ml/7278/category/618/display/1/'
    ]
    clean_dir('images/')
    url = urls[1]
    thumbnail_xpath = "//div[@class='thumbnail']/img"
    detail_xpath = "//div[@class='cont']/div/img"
    scrapper = ImageScrapper(url)
    scrapper.scrap(xpath=thumbnail_xpath)
    scrapper.scrap(xpath=detail_xpath)
    pass