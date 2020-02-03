from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Sachin/Desktop/chromedriver.exe')
driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')

count = int(input('Enter the count : '))
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(randomString())
    driver.find_element_by_class_name('_3M-N-').click()
