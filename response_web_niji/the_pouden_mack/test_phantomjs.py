

from selenium import webdriver
webdriver = webdriver.PhantomJS(executable_path=r'E:\JetBrains\TEST_Project\Test_selenium_response\phantomjs-2.1.1\phantomjs-2.1.1-windows\bin\phantomjs.exe')
webdriver.get("https://www.baidu.com")
print(webdriver.page_source)