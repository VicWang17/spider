import selenium.webdriver as webdriver
import pickle

# 创建浏览器对象
browser = webdriver.Chrome()

# 在浏览器中登录并获取cookie
browser.get('https://www.lagou.com/')
s=input()
if s:
    pass
cookie = browser.get_cookies()
with open('cookie.pickle', 'wb') as f:
    pickle.dump(cookie, f)
