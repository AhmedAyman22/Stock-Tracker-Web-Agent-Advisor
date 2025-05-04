# COMPANIES WITH TOP 100 MARKET CAP IN THE NASDAQ STOCK MARKET SCRAPER

from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json
import os


def scraper():
    service = Service(cdm().install())
    headless = Options()
    headless.add_argument('--headless')
    headless.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36") # Example user-agent    
    driver = wd.Chrome(service=service, options=headless)
    driver.get('https://www.nasdaq.com/market-activity/stocks/screener?page=1&rows_per_page=100')
    time.sleep(5)
    topCompanies = {}
    try:
        for i in range(1, 101):
            company_xpath = f'/html/body/div[2]/div/main/div[2]/article/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/table/tbody/tr[{i}]/td[2]/a'
            ticker_xpath = f'/html/body/div[2]/div/main/div[2]/article/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/table/tbody/tr[{i}]/td[1]/a'
            companyName = driver.find_element(By.XPATH, company_xpath).text
            companyTicker = driver.find_element(By.XPATH, ticker_xpath).text
            topCompanies[str(i)] = {
                'name': companyName,
                'ticker': companyTicker
            }
        print('data fetched')
        # Save the data to a JSON file
        cur_path = os.path.dirname(__file__)
        new_path = os.path.relpath('..\\data\\data.json', cur_path)
        
        with open(new_path, 'w') as json_file:
            json.dump(topCompanies, json_file, indent=4)        
    
        print("Data saved to '\\Stock-Tracker-Web-Agent-Advisor\\data\\data.json'")  
    
    except ValueError:
        print('ValueError')
    except IndexError:
        print('IndexError')
    finally:
        driver.quit()  

scraper()