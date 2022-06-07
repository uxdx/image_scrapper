import requests
import os
from os.path  import basename

def get_files_in_dir(path:str)->list:
    return os.listdir(path)
    
def clean_dir(path:str):
    files_in_dir = get_files_in_dir(path)
    for file in files_in_dir:
        os.remove(path+file)
        print(path+file, 'is removed.')
    print('Clear succeed.')

def download_images(src:str, path:str, filename:str) -> int:
    """
        src 경로로 파일을 내려받아 경로에 파일이름으로 저장하는 함수
        성공시 1, 실패시 -1을 반환
    """
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
        }
    r = requests.get(src,headers=headers)
    # print(r.content)
    if r.status_code == 200:
        with open(path+filename, 'wb') as f:
            print('write in '+path+filename)
            f.write(r.content)
        return 1
    print('download fail.')
    print(src)
    print(r)
    return -1
    # os.system("curl " + src + " > "+filename)

def get_image_extension(string:str) -> str:
    """
        파일 확장자를 추출하는 함수
        확장자가 검출되지 않는 경우 빈 문자열을 반환
    """
    extension_list = ['.jpg', '.png', '.gif', '.jpeg']
    for extension in extension_list:
        if extension in string:
            return extension
    return ''

def get_filename_from_url(url:str) -> str:
    """
        파일 이름을 추출하는 함수 
        확장자가 검출되지 않으면 빈 문자열을 반환
    """
    if len(get_image_extension(url)) == 0:
        return ''
    splited_url = url.split('/') # 경로로 
    filename = splited_url[len(splited_url)-1].split('.')[0]
    return filename

def get_filename_include_extension(url:str) -> str:
    """
        확장자를 포함하는 파일명 추출
    """
    if len(get_image_extension(url)) == 0:
        return ''
    return url.split('/')[-1]
            

if __name__ == '__main__':
    sample_url = 'https://www.coupang.com/vp/products/2040637002?itemId=3469208914&vendorItemId=71455552336&isAddedCart='
    url = 'https://image6.coupangcdn.com/image/badges/cashback/web/list-cash-icon@2x.png'
    # download_images(src='https://image6.coupangcdn.com/image/badges/cashback/web/list-cash-icon@2x.png',path='images\\',filename='test.png')
    
    # print(get_filename_from_url(url))