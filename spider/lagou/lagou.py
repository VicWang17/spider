from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time 
import pickle

def login(url,driver):
    with open('cookie.pickle', 'rb') as f:
        cookie = pickle.load(f)  
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"cboxClose").click()
    time.sleep(8)
    driver.find_element(By.XPATH,'//*[@id="lg_tbar"]/div[1]/div[2]/ul/li[1]/a').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[2]/div[3]/div').click()
    time.sleep(0.2)
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/input').send_keys("13817177808")
    time.sleep(0.3)
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/input').send_keys('594Wyh517.')
    time.sleep(0.2)
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div/div[2]/div/div[2]/div[3]/div[2]/button').click()
    wait = input()
    if wait:
        pass
def get_page(ans,driver):
    #driver.implicitly_wait(10)
    #driver.find_element(By.ID,"cboxClose").click()
    time.sleep(2)
    driver.find_element(By.ID,"search_input").send_keys(ans)
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"search_button").click()
    

def get_info(i,ans,driver):
    global total
    global num
    driver.get('https://www.lagou.com/wn/jobs?pn={}&cl=false&fromSearch=true&labelWords=sug&suginput={}&kd={}'.format(str(i),ans,ans))
    time.sleep(2)
    names = driver.find_elements(By.ID,"openWinPostion")
    salarys = driver.find_elements(By.CLASS_NAME,"money__3Lkgq")
    for j in range(0,len(names)):
        try:
            print(names[j].text,salarys[j].text)
            mon = salarys[j].text
            mon = mon.split('-')
            total+=(int(mon[0][0:-1])*1000+int(mon[1][0:-1])*1000)/2
            num+=1
        except StaleElementReferenceException:
            print("There is some error.")



if __name__=='__main__':
    total=0
    num=0
    ans = input("你想要检索的职业是：")
    url = 'https://www.lagou.com/'
    driver = webdriver.Chrome()
    driver.maximize_window()    
    login(url,driver)
    get_page(ans,driver)
    for i in range(1,30):
        print('以下是第'+str(i)+'页的资料')
        get_info(i,ans,driver)
    print(ans+"这一行的平均工资是"+str(total/num))


    