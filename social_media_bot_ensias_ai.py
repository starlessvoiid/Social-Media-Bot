import os
if os.path.isfile("C://Users//adnaneeee//Desktop//social_media_bot_ensias_ai//config//0620479277_uuid_and_cookie.json"):
    os.remove("C://Users//adnaneeee//Desktop//social_media_bot_ensias_ai//config//0620479277_uuid_and_cookie.json")
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen
from time import sleep
import pyautogui


def login_fb(username, password):

    try :
        url = 'https://facebook.com'
        driver.get(url)
        user = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'email')))
        user.send_keys(username)
        pas = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'pass')))
        pas.send_keys(password)
        login_btn = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'login')))
        login_btn.click()

    except :
        print('Something went wrong while login process')

def upload_fb(img_path,caption):
    try :
        btn1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/div[1]/span/div/i')))
        btn1.click()
        btn2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/i')))
        btn2.click()
        btn3 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div/div/div[1]/div/div/div[1]/i')))
        btn3.click()
        btn4 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div')))
        btn4.click()
        pyautogui.write(img_path)
        pyautogui.press('enter')
        cap = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div')))
        cap.send_keys(caption)
        sleep(10)
        btn_post = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span')))
        btn_post.click()
    except :
        print('Something went wrong while posting the image or video')
        
def login_insta(username, password) :
    try :
        url = 'https://instagram.com'
        driver.get(url)
        user = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'username')))
        user.send_keys(username)
        pas = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'password')))
        pas.send_keys(password)
        login_btn = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')))
        login_btn.click()

    except :
        print('Something went wrong while login process')
def upload_insta(img_path, caption) :
    try :
        btn1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button')))
        btn1.click()
        btn2 = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')))
        btn2.click()
        pyautogui.write(img_path)
        pyautogui.press('enter')
        btn3 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')))
        btn3.click()
        btn4 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')))
        btn4.click()
        cap = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea')))
        cap.send_keys(caption)
        sleep(10)
        btn_post = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')))
        btn_post.click()
    except :
        print('Something went wrong while posting the image or video')
if __name__== "__main__":
    user = '0620479277'
    passwd = 'botpass'
    img_path = input('ENTER IMAGE NAME : ')
    location = "images"
    full_img_path = os.path.join(location, img_path)
    caption = input('ENTER CAPTION : ')
    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    #login_fb(username,password)
    #upload_fb(full_img_path,caption)
    login_insta(user, passwd)
    upload_insta(full_img_path, caption)
    
