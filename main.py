from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random
import re
import pandas as pd
import numpy as np

from datetime import datetime

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
)

import os.path
from os.path import dirname, join
import socket
import csv
import pyperclip as pc
import pyautogui
import io


input_link = input("Enter link : ")
output_file_name = input("Enter outputt file name ")

error_page_links = []

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)  # version_main allows to specify your chrome version instead of following chrome global version
driver.maximize_window()


driver.get(input_link)  

time.sleep(6)

html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

page_numbers = []
Last_page = 0

for btn in soup.find_all('button', attrs={"data-page": True}):
    print(btn["data-page"])
    page_numbers.append(int(btn["data-page"]))

print(page_numbers)
Last_page = max(page_numbers)

print(Last_page)
#Last_page = 4

job_links = []

title = []
company_name = []
company_location = []
job_title = []
job_content = []
job_publish_date = []

calender_txt = []
duration_txt = []
experience_txt = []
location_txt = []
salary_txt = []
telecommunication_txt = []


for i in range(Last_page):
    try:
        print(i+1)
        driver.get(input_link+"?page="+str(i+1))

        time.sleep(4)
        html = driver.page_source
        soup = BeautifulSoup(html, features="html.parser")

        try:
            search_div = soup.find("div", attrs={"data-testid" : "search-result"})

            for a in search_div.find_all('a', href=True):
                if "/fr/" in a['href']:
                    try:
                        
                        driver.get('https://www.free-work.com'+a['href'])  
                        time.sleep(4)

                        html = driver.page_source

                        soup = BeautifulSoup(html, features="html.parser")

                        header = soup.find('div', attrs={"class" : "text-white w-full"}).get_text(separator="\n")

                        my_header_text = []

                        for item in header.split('\n'):
                                    if len(item.strip()) > 0:
                                        my_header_text.append(item.strip())

                        try:
                            m_title = my_header_text[0]
                        except:
                            m_title = ""

                        try:    
                            m_company_name = my_header_text[1]
                        except:
                            m_company_name = ""

                        try:    
                            m_company_location = my_header_text[2]
                        except:
                            m_company_location = ""

                        try:    
                            m_job_title = my_header_text[3]
                        except:
                            m_job_title = ""

                        try:
                            my_time = soup.find('time', attrs={"class" : "text-sm w-full"}).text.strip()
                        except:
                            my_time = ""

                        
                        page_content = soup.find('div', attrs={"class" : "prose-content"}).get_text(separator="\n").split('\n')
                        
                        my_page_content = "\n".join(page_content)

                        m_job_content = my_page_content

                        m_calender_txt = ""
                        m_duration_txt =""
                        m_experience_txt = ""
                        m_location_txt = ""
                        m_salary_txt = ""
                        m_telecommunication_txt =""

                        calendar_icon_path = "M152 64H296V24C296 10.75 306.7 0 320 0C333.3 0 344 10.75 344 24V64H384C419.3 64 448 92.65 448 128V448C448 483.3 419.3 512 384 512H64C28.65 512 0 483.3 0 448V128C0 92.65 28.65 64 64 64H104V24C104 10.75 114.7 0 128 0C141.3 0 152 10.75 152 24V64zM48 448C48 456.8 55.16 464 64 464H384C392.8 464 400 456.8 400 448V192H48V448z"

                        duration_icon_path = "M232 120C232 106.7 242.7 96 256 96C269.3 96 280 106.7 280 120V243.2L365.3 300C376.3 307.4 379.3 322.3 371.1 333.3C364.6 344.3 349.7 347.3 338.7 339.1L242.7 275.1C236 271.5 232 264 232 255.1L232 120zM256 0C397.4 0 512 114.6 512 256C512 397.4 397.4 512 256 512C114.6 512 0 397.4 0 256C0 114.6 114.6 0 256 0zM48 256C48 370.9 141.1 464 256 464C370.9 464 464 370.9 464 256C464 141.1 370.9 48 256 48C141.1 48 48 141.1 48 256z"

                        experience_icon_path = "M448 96h-64V64c0-35.35-28.65-64-64-64H192C156.7 0 128 28.65 128 64v32H64C28.65 96 0 124.7 0 160v256c0 35.35 28.65 64 64 64h384c35.35 0 64-28.65 64-64V160C512 124.7 483.3 96 448 96zM176 64c0-8.838 7.164-16 16-16h128c8.836 0 16 7.162 16 16v32h-160V64zM464 416c0 8.799-7.199 16-16 16H64c-8.801 0-16-7.201-16-16V160c0-8.801 7.199-16 16-16h384c8.801 0 16 7.199 16 16V416z"

                        location_icon_path = "M168.3 499.2C116.1 435 0 279.4 0 192C0 85.96 85.96 0 192 0C298 0 384 85.96 384 192C384 279.4 267 435 215.7 499.2C203.4 514.5 180.6 514.5 168.3 499.2H168.3zM320.7 249.2C331.5 223.6 336 204.4 336 192C336 112.5 271.5 48 192 48C112.5 48 48 112.5 48 192C48 204.4 52.49 223.6 63.3 249.2C73.78 274 88.66 301.4 105.8 329.1C134.2 375.3 167.2 419.1 192 451.7C216.8 419.1 249.8 375.3 278.2 329.1C295.3 301.4 310.2 274 320.7 249.2V249.2z"

                        salary_icon_path = "M456 32C469.3 32 480 42.75 480 56C480 69.25 469.3 80 456 80H88C65.91 80 48 97.91 48 120V392C48 414.1 65.91 432 88 432H424C446.1 432 464 414.1 464 392V216C464 193.9 446.1 176 424 176H120C106.7 176 96 165.3 96 152C96 138.7 106.7 128 120 128H424C472.6 128 512 167.4 512 216V392C512 440.6 472.6 480 424 480H88C39.4 480 0 440.6 0 392V120C0 71.4 39.4 32 88 32H456zM352 304C352 286.3 366.3 272 384 272C401.7 272 416 286.3 416 304C416 321.7 401.7 336 384 336C366.3 336 352 321.7 352 304z"

                        telecommunication_icon_path = "M224.8 5.394C233.7-1.798 246.3-1.798 255.2 5.394L471.2 181.4C481.4 189.8 482.1 204.9 474.6 215.2C466.2 225.4 451.1 226.1 440.8 218.6L416 198.4V240H368V159.3L240 54.96L112 159.3V360C112 364.4 115.6 368 120 368H272V416H120C89.07 416 64 390.9 64 360V198.4L39.16 218.6C28.89 226.1 13.77 225.4 5.395 215.2C-2.978 204.9-1.435 189.8 8.841 181.4L224.8 5.394zM288 216V261.7C281.1 268.5 277.4 276.6 274.7 285.5C271.5 287.1 267.9 288 264 288H216C202.7 288 192 277.3 192 264V216C192 202.7 202.7 192 216 192H264C277.3 192 288 202.7 288 216zM336 272H560C577.7 272 592 286.3 592 304V464H628C634.6 464 640 469.4 640 476C640 495.9 623.9 512 604 512H292C272.1 512 256 495.9 256 476C256 469.4 261.4 464 268 464H304V304C304 286.3 318.3 272 336 272zM352 320V464H544V320H352z"

                        point_container = soup.findAll("div", attrs={"class": "flex items-center py-1"})
                        for p_c in point_container:
                            s_icn = p_c.find("path", attrs={"d": True})

                            if s_icn["d"] == calendar_icon_path :
                                #print("Calender")
                                try:
                                    m_calender_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_calender_txt = ""
                            elif s_icn["d"] == duration_icon_path:
                                #print("Duration")
                                try:
                                    m_duration_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_duration_txt = ""
                            elif s_icn["d"] == experience_icon_path:
                                #print("Experience")
                                try:
                                    m_experience_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_experience_txt = ""
                            elif s_icn["d"] == location_icon_path:
                                #print("Location")
                                try:
                                    m_location_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_location_txt = ""
                            elif s_icn["d"] == salary_icon_path:
                                #print("Salary")
                                try:
                                    m_salary_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_salary_txt = ""
                            elif s_icn["d"] == telecommunication_icon_path:
                                #print("Telecommunication")
                                try:
                                    m_telecommunication_txt = p_c.find("span", attrs={"class": "w-full text-sm line-clamp-2"}).text.strip()
                                except:
                                    m_telecommunication_txt = ""
                    
                        job_links.append('https://www.free-work.com'+a['href'])
                        title.append(m_title)
                        company_name.append(m_company_name)
                        company_location.append(m_company_location)
                        job_title.append(m_job_title)
                        job_publish_date.append(my_time)
                        job_content.append(m_job_content)

                        calender_txt.append(m_calender_txt)
                        duration_txt.append(m_duration_txt)
                        experience_txt.append(m_experience_txt)
                        location_txt.append(m_location_txt)
                        salary_txt.append(m_salary_txt)
                        telecommunication_txt.append(m_telecommunication_txt)


                        file_pandas = pd.DataFrame({
                                "Job link" : np.array(job_links),
                                "Title" : np.array(title),
                                "Company Name" : np.array(company_name),
                                "Company Location" : np.array(company_location),
                                "Job title" : np.array(job_title),
                                "Job publish date" : np.array(job_publish_date),
                                "Job content" : np.array(job_content),
                                "Joining Date" : np.array(calender_txt),
                                "Duration" : np.array(duration_txt),
                                "Experience Requirement": np.array(experience_txt),
                                "Telicommunication" : np.array(telecommunication_txt),
                                "Location" : np.array(location_txt),
                                "Salary" : np.array(salary_txt)
                        })


                        file_pandas.to_csv(output_file_name+".csv", index=False, encoding='utf-8-sig')    

                    except Exception as e:
                        print(e)     
                    
        except:
            print("--------------------------------------")
    except:
        print("Oops error at page = "+str(i+1))

        error_page_links.append(str(i+1))
        error_page_links_pandas = pd.DataFrame({
                        "Page Error link" : np.array(error_page_links)
                    })

        error_page_links_pandas.to_csv(output_file_name+"_error_links.csv", index=False, encoding='utf-8-sig')
