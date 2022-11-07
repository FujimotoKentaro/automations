from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("user-data-dir=" + '/Users/seijimurai/Library/Application Support/Google/Chrome/Default')

driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.co.jp/")
