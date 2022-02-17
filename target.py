import re
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import threading
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import pandas as pd
import multiprocessing
warnings.filterwarnings("ignore")


def level_one(username, password):
    source_url = 'https://alt.s4labour.com/Account/LogOn'
    log_file = open('D:\Users\Divyapriya\PycharmProjects1\PythonTesting\level_one_log_file.txt', 'w')

    date = datetime.now().date()
    log_file.writelines(str(date))
    log_file.writelines("\n")
    driver=webdriver.Chrome(executable_path=r"D:\Users\Divyapriya\PycharmProjects1\PythonTesting\chromedriver.exe")
    driver.get(source_url)
    try:
        user_name = driver.find_element_by_xpath("//input[@id='Username']")
        user_name.send_keys(username)
        print('username_ok')
        pass_word = driver.find_element_by_xpath("//input[@id='Password']")
        pass_word.send_keys(password)
        login = driver.find_element_by_xpath("//input[@type='submit']")
        login.click()
        print("username, password done")
        log_file.writelines("username, password done")
        log_file.writelines("\n")
        time.sleep(2)
        # try:
        #     continue_button = driver.find_element_by_xpath("//input[@value='Continue']")
        #     continue_button.click()
        # except Exception as continue_button_error:
        #     print(continue_button_error)
        #     log_file.writelines(str(continue_button_error))
        #     log_file.writelines("\n")
        # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Switch to Employee profile']"))))
        # driver.find_element_by_xpath("//a[text()='View my rota']").click()
        driver.find_element_by_xpath(("//a[text()='Export to Excel']")).click()
        time.sleep(2)
        log_file.writelines("Export to Excel done")
        log_file.writelines("\n")
        log_file.writelines('************************************')
        log_file.close()
    except Exception as error:
        print(error)
        log_file.writelines(str(error))
        log_file.writelines("\n")
        log_file.writelines('************************************')
        log_file.close()
        driver.close()
    driver.close()

def level_two(username, password):
    log_file = open('D:\Users\Divyapriya\PycharmProjects1\PythonTesting\level_two_log_file.txt', 'w')
    date = datetime.now().date()
    log_file.writelines(str(date))
    log_file.writelines("\n")
    try:
        driver = webdriver.Chrome(executable_path=r"D:\Users\Divyapriya\PycharmProjects1\PythonTesting\chromedriver.exe")
        source_url = 'https://alt.s4labour.com/Account/LogOn'
        driver.get(source_url)
    except Exception as driver_error:
        print(driver_error)
        log_file.writelines('chrome_driver_ERROR!!!')
        log_file.writelines("\n")
    try:
        try:
            user_name = driver.find_element_by_xpath("//input[@id='Username']")
            user_name.send_keys(username)
            print('username_ok')
            pass_word = driver.find_element_by_xpath("//input[@id='Password']")
            pass_word.send_keys(password)

            login = driver.find_element_by_xpath("//input[@type='submit']")
            login.click()
            time.sleep(2)
            print("username, password done")
            log_file.writelines("username, password done")
            log_file.writelines("\n")
        except Exception as login_error:
            print(login_error)
            log_file.writelines(str(login_error))
            log_file.writelines("\n")
            driver.close()
        try:
            driver.find_element_by_xpath("(//a[text()='View'])[1]").click()
            time.sleep(5)
        except Exception as view_error:
            print(view_error)
            log_file.writelines(str(view_error))
            log_file.writelines("\n")
            driver.close()
        # driver.find_element_by_xpath("(//a[text()='Approve'])[1]").click()
        # time.sleep(5)
        # a = Alert(driver)
        # a.accept()
        # a.dismiss()
        # driver.find_element_by_xpath("(//a[text()='Reject'])[1]']").click()
        time.sleep(3)
    except Exception as error:
        print(error)
        driver.close()
        log_file.writelines("\n")
        log_file.writelines('************************************')
    driver.close()
    log_file.writelines("\n")
    log_file.writelines('************************************')

def level_three(username, password):
    log_file = open('D:\Users\Divyapriya\PycharmProjects1\PythonTesting\level_three_log_file.txt', 'w')
    date = datetime.now().date()
    log_file.writelines(str(date))
    log_file.writelines("\n")
    try:
        driver=webdriver.Chrome(executable_path=r"D:\Users\Divyapriya\PycharmProjects1\PythonTesting\chromedriver.exe")
        source_url = 'https://alt.s4labour.com/Account/LogOn'
        driver.get(source_url)
    except Exception as driver_error:
        print(driver_error)
        log_file.writelines('chrome_driver_ERROR!!!')
        log_file.writelines("\n")
    try:
        try:
            user_name = driver.find_element_by_xpath("//input[@id='Username']")
            user_name.send_keys(username)
            print('username_ok')
            pass_word = driver.find_element_by_xpath("//input[@id='Password']")
            pass_word.send_keys(password)

            login = driver.find_element_by_xpath("//input[@type='submit']")
            login.click()
            time.sleep(2)
            print("username, password done")
            log_file.writelines("username, password done")
            log_file.writelines("\n")
        except Exception as login_error:
            print(login_error)
            log_file.writelines(str(login_error))
            log_file.writelines("\n")
            driver.close()
        action = ActionChains(driver)
        action.move_to_element(driver.find_element_by_xpath("//div[@id='header']/div[1]/div[2]/div[2]")).perform()
        driver.find_element_by_xpath("//a[text()='Rota - Current Week']").click()
        time.sleep(10)
        # driver.find_element_by_xpath("//a[text()='Flag forecast rota as complete']").click()
        driver.find_element_by_xpath("//a[@id='FlagActual']").click()
        a = Alert(driver)
        a.accept()
    except Exception as error:
        print(error)
        log_file.writelines(str(error))
        driver.close()
        log_file.writelines("\n")
        log_file.writelines('************************************')
    driver.close()
    log_file.writelines("\n")
    log_file.writelines('************************************')

if __name__=='__main__':
    input_path = 'D:\Users\Divyapriya\PycharmProjects1\PythonTesting\input.xlsx'
    input_df = pd.read_excel(input_path)
    for index, row in input_df.iterrows():
        if row['user_type'] == 'level_1':
            print('level_1')
            driver_thread1 = threading.Thread(target=level_one, args=(row['username'], row['password']))
            driver_thread1.start()
            # driver_thread1.join()
        elif row['user_type'] == 'level_2':
            print('level_2')
            driver_thread2 = threading.Thread(target=level_two, args=(row['username'], row['password']))
            driver_thread2.start()
        elif row['user_type'] == 'level_3':
            print('level_3')
            driver_thread3 = threading.Thread(target=level_three, args=(row['username'], row['password']))
            driver_thread3.start()
