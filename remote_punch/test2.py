from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from tenacity import retry, stop_after_delay, wait_fixed
import time
import subprocess

port = 9222
p = subprocess.run(["open","-a","/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--args",
                    f"--remote-debugging-port={port}"])
time.sleep(5)
options = Options()
options.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
options.add_argument("--user-data-dir=" + "/Users/opm005789/Library/Application Support/Google/Chrome/Default")
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
time.sleep(1)
driver.execute_script('alert("test")')
time.sleep(10)
# driver.quit()