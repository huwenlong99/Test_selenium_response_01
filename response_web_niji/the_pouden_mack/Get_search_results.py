#  获取搜索结果Get search results

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


# 声明谷歌、Firefox、Safari等浏览器
browser = webdriver.Chrome()
# browser= webdriver.Firefox()
# browser= webdriver.Safari()
# browser= webdriver.Edge()
# browser= webdriver.PhantomJS()

# 打开浏览器，输入白底地址，输入要搜索的值，点击搜索

try:
    url = "https://www.baidu.com"
    browser.get(url)
    input = browser.find_element_by_id("kw")
    input.send_keys("外骨骼")
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(10)
finally:
    print(url.format(1, ))
    browser.close()


#  查找单个元素

"""
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element(By.ID, "q")
print(input_first , input_second, input_first)
"""