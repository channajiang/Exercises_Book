# https://www.cnblogs.com/poloyy/category/1680176.html?page=1


import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'https://www.vmall.com/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
# //ol[@class="category-list"]表示一个元素中包含了十个li， 需要定位到li,再遍历他们
first_elements = driver.find_elements(By.XPATH, '//ol[@class="category-list"]/li')
time.sleep(3)
for i in first_elements:
    print('一级菜单： %s' % i.text)
    ActionChains(driver).move_to_element(i).perform()
    time.sleep(1)
    # /li[@class="subcate-item"]可以过滤掉一部分不必要的元素，定位时可对比下有这层过滤和无这层过滤的数量
    second_elements = i.find_elements(By.XPATH, './/ul[@class="subcate-list clearfix"]/li[@class="subcate-item"]')
    time.sleep(1)
    for j in second_elements:
        print('  二级菜单： %s' % j.text)
js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)
hot_eles = driver.find_elements(By.XPATH, '//li[@class="grid-items"]//p[@class="grid-tips"]')
for k in hot_eles:
    if k.text == '热销爆款':
        # 产品名字和价格与目标元素k的关系是同一个爸爸，所以需要定位k与产品名字/价格的共同爸爸./../，再找他们爸爸底下的相关产品名字/价格
        name = k.find_element(By.XPATH, './../div[@class="grid-title"]').text
        price = k.find_element(By.XPATH, './../p[@class="grid-price"]').text
        print(k.text + ':' + name + '价格' + price)


driver.quit()