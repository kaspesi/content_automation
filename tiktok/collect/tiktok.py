import time
import threading
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib import parse


class Tiktok:

    def __init__(self, url):
        print('Tiktok init')
        self.url = "https://www.tiktok.com/"
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        self.get_clip_urls()

    def __str__(self) -> str:
        retString = ""
        retString += "Site: [" + self.url + "]"
        for article in self.articles:
            retString += str(article) + '\n\n'
        return retString

    @staticmethod
    def format_url(url):
        i = url.index('www.tiktok.com')
        url = url[i::]
        return parse.unquote(url)

    def get_post_data(self, button_group):
        text_elem = button_group.find_element(By.XPATH, "./../..")
        if('Paid partnership' in text_elem.text):
            print('Paid partnership: skipping post data')
            return
        video_desc_elem = text_elem.find_element(By.XPATH, ".//div[@data-e2e = 'video-desc']")
        caption = video_desc_elem.find_element(By.XPATH, "./span").text
        tags = [elem.text for elem in video_desc_elem.find_elements(By.XPATH, "./a")]
        print('CAPTION')
        print(caption)
        print('TAGS')
        print(tags)
        like_count = button_group.find_element(By.XPATH, ".//strong[@data-e2e = 'like-count']").text
        comment_count = button_group.find_element(By.XPATH, ".//strong[@data-e2e = 'comment-count']").text
        share_count = button_group.find_element(By.XPATH, ".//strong[@data-e2e = 'share-count']").text
        print(like_count, comment_count, share_count)
        share_button = button_group.find_element(By.XPATH, ".//strong[@data-e2e = 'share-count']/parent::*")
        share_button.click()
        share_url = self.driver.find_element(By.XPATH, ".//a[@data-e2e = 'video-share-whatsapp']").get_attribute('href')
        print(Tiktok.format_url(share_url))
        download_url = self.get_download_url(share_url)
        print(download_url)

    def get_posts_data(self, button_groups):
        for button_group in button_groups:
            print(button_group.text)
            self.get_post_data(button_group)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button_group)
            time.sleep(5)
        

    def get_clip_urls(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 20, poll_frequency=1)
        elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'TikTok')]")))
        time.sleep(5)
        html = self.driver.page_source
        # print(html)
        buttons = self.driver.find_elements(By.XPATH, "//button[.//span[@data-e2e = 'share-icon']]/parent::*")
        print(len(buttons))
        self.get_posts_data(buttons)

        # button1 = buttons[0]
        # print(button1.get_attribute('innerHTML'))

        with open('tiktok.html', 'w') as f:
            for button in buttons:
                f.write(f"{button.text}\n")
        self.driver.quit()
    
    def get_download_url(self, share_url):
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #'cookie': 'current_language=en; _ga=GA1.1.115940210.1660795490; _gcl_au=1.1.669324151.1660795490; _ga_5370HT04Z3=GS1.1.1660795489.1.1.1660795513.0.0.0',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
        data = {
            "url": share_url,
            "count": 12,
            "cursor": 0,
            "web": 1,
            "hd": 1
        }

        response = requests.post("https://www.tikwm.com/api/", headers=headers, data=data).json()
        print(response)
        download_url = "https://www.tikwm.com/" + response["data"]["hdplay"] if response["data"]["hdplay"] else response["data"]["play"]
        
        return download_url

