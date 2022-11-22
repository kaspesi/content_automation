import time
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
        text_data = button_group.find_element(By.XPATH, "./../..")
        text_desc = button_group.find_element(By.XPATH, "//div[@data-e2e = 'video-desc']//span").text
        text_desc_tags = button_group.find_element(By.XPATH, "//div[@data-e2e = 'video-desc']//a").text
        if('Paid partnership' in text_data.text):
            print('Paid partnership: canceling')
            return
        print('TITLE')
        print(text_desc)
        print('TAGS')
        print(text_desc_tags)
        like_count = button_group.find_element(By.XPATH, "//strong[@data-e2e = 'like-count']").text
        comment_count = button_group.find_element(By.XPATH, "//strong[@data-e2e = 'comment-count']").text
        share_count = button_group.find_element(By.XPATH, "//strong[@data-e2e = 'share-count']").text
        print(like_count, comment_count, share_count)
        share_button = button_group.find_element(By.XPATH, "//strong[@data-e2e = 'share-count']/parent::*")
        share_button.click()
        video_link = self.driver.find_element(By.XPATH, "//a[@data-e2e = 'video-share-whatsapp']").get_attribute('href')
        print(Tiktok.format_url(video_link))

    def get_posts_data(self, button_groups):
        for button_group in button_groups:
            print(button_group.text)
            self.get_post_data(button_group)
        

    def get_clip_urls(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 20, poll_frequency=1)
        elem = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'TikTok')]")))
        time.sleep(5)
        html = self.driver.page_source
        # print(html)
        buttons = self.driver.find_elements(By.XPATH, "//button[.//span[@data-e2e = 'share-icon']]/parent::*")
        print(len(buttons))
        # self.get_posts_data(buttons)

        # button1 = buttons[0]
        # print(button1.get_attribute('innerHTML'))

        with open('tiktok.html', 'w') as f:
            f.write(buttons.text)
        self.driver.quit()
