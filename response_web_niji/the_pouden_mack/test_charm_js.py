# 使用selenium的方法打开谷歌浏览器     查询


from selenium import webdriver
webdriver = webdriver.Chrome()
webdriver.get("https://www.baidu.com")
print(webdriver.page_source)

