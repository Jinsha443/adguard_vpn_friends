from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from pymailtm import MailTm
import names, time, random, string, uuid, threading

link = input("Your link: ")

def password_gen(password=""):
    characters = string.ascii_letters + string.digits

    for _ in range(random.randint(12,18)):
        password = password + random.choice(characters)

    return password

def type_keys(obj, text):
    obj.click()
    time.sleep(0.5)
    for i in text:
        obj.send_keys(i)
        time.sleep(random.uniform(0.2, 0.111111))

def main():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-audio-output")
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service("./chromedriver"), options=options)

    driver.get(link)
    driver.find_element(by=By.CLASS_NAME, value="promo__btn").click()

    acc = MailTm().get_account()
    type_keys(driver.find_element(by=By.CLASS_NAME, value="jsauth-input_email"), acc.address)
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="jsauth-button_primary").click()
    time.sleep(2)

    password = password_gen()
    type_keys(driver.find_element(value="password"), password)
    type_keys(driver.find_element(value="repeat-password"), password)
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="jsauth-button_primary").click()
    time.sleep(2)

for i in range(5):
    main()
