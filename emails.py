from selenium import webdriver
import time

url = 'https://protonmail.com/'
url_signup_free='https://mail.protonmail.com/create/new?language=en'
driver = webdriver.Chrome('/Users/johnfisher/Downloads/chromedriver')
driver.get(url_signup_free)

time.sleep(2)
#switching to frame 
driver.switch_to.frame(driver.find_element_by_class_name("top"))
driver.find_element_by_xpath("//*[@id='username']").send_keys('usernameForUser')
driver.switch_to.default_content()

time.sleep(1.5)

driver.find_element_by_xpath('//*[@id="password"]').send_keys('passwordForUser')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="passwordc"]').send_keys('passwordForUser')

time.sleep(2)

driver.switch_to.frame(driver.find_element_by_class_name("bottom"))
driver.find_element_by_xpath('/html/body/div[1]/div/footer/button').click()
driver.switch_to.default_content()

time.sleep(1)

driver.find_element_by_id('confirmModalBtn').click()

time.sleep(1)

driver.find_element_by_xpath('//*[@id="emailVerification"]').send_keys('mailid')

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div/div/form[1]/div[1]/div[2]/button').click()































