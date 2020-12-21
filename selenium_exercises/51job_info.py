import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# http://vip.ytesting.com/q.do?a&id=ff8080817238543f01723b6246cc011e

driver = webdriver.Chrome()
url = 'https://www.51job.com/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

# 点击高级搜索
search = driver.find_element(By.XPATH, '//a[@class="more"]').click()

# 输入python
input = driver.find_element(By.XPATH, '//p[@class="ipt"]/input[@type="text"]')
input.click()
input.send_keys('python')

# 点击地区按键
locale_btn = driver.find_element(By.XPATH, '//p[@class="addbut"]/input[@type="button"]')
locale_btn.click()

# 清除已选地区
time.sleep(5)
driver.find_element(By.XPATH, '//span[@class="ttag"]').click()
time.sleep(5)

# 点击杭州
driver.find_element(By.ID, 'work_position_click_center_right_list_category_000000_080200').click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[@id="work_position_click_bottom_save"]').click()
# 点击高级搜索，清除python输入框的下拉列表
driver.find_element(By.XPATH, '//div[@class="tit"]/span').click()
time.sleep(5)

# 点击职能类别
driver.find_element(By.XPATH, '//span[@id="funtype_click"]').click()
time.sleep(5)

# 点击高级软件工程师
driver.find_element(By.ID, 'funtype_click_center_right_list_category_0100_0100').click()
time.sleep(5)
driver.find_element(By.ID, 'funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element(By.ID, 'funtype_click_bottom_save').click()
time.sleep(5)

# 点击1-3年
driver.find_element(By.XPATH, '//div[@id="workyear_list"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//span[@title="1-3年"]').click()

# 点击搜索
driver.find_element(By.XPATH, '//div[@class="btnbox p_sou"]/span').click()

# 获取工作信息表
job_list = driver.find_elements(By.XPATH, '//div[@class="j_joblist"]/div')

for info in job_list:
    # print(info.text)
    # job_name = info.find_element(By.XPATH, '//div[@class="j_joblist"]/div/a/p[@class="t"]')
    # com_name = info.find_element(By.XPATH, '//div[@class="j_joblist"]/div/div[@class="er"]/a')
    # location_01 = info.find_element(By.XPATH, '//div[@class="j_joblist"]/div/a/p[@class="info"]/span[@class="d at"]') # 多了信息
    # # location = location_01.text
    # salary = info.find_element(By.XPATH, '//div[@class="j_joblist"]//div/a/p[@class="info"]/span[@class="sal"]')
    # time = info.find_element(By.XPATH, '//div[@class="j_joblist"]/div/a/p[@class="t"]/span[@class="time"]')

    # 根据以上xpath路径观察得出： 以下信息的元素全部都在//div[@class="j_joblist"]/div下面，因此用./表示
    job_name = info.find_element(By.XPATH, './a/p[@class="t"]/span[@class="jname at"]')
    com_name = info.find_element(By.XPATH, './div[@class="er"]/a')
    location_01 = info.find_element(By.XPATH, './a/p[@class="info"]/span[@class="d at"]') # 获取了额外不需要的信息
    # 切割并截取所需要的信息
    location = location_01.text.split('|', 1)
    salary = info.find_element(By.XPATH, './a/p[@class="info"]/span[@class="sal"]')
    time = info.find_element(By.XPATH, './a/p[@class="t"]/span[@class="time"]')
    print(job_name.text, '|', com_name.text, '|', location[0], '|', salary.text, '|', time.text)


driver.quit()