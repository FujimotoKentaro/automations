from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import subprocess

port = 9222
p = subprocess.run(["open","-a","/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--args",
                    f"--remote-debugging-port={port}"])
time.sleep(5)
options = Options()
options.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
# options.add_argument("--user-data-dir=" + "/Users/opm005789/Library/Application Support/Google/Chrome/Default")
# options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(options=options)

# teamspiritのリンク
# driver.get("https://optimcorporation.okta.com/app/salesforce/exk1hk8n5ic3Jj2XT0h8/sso/saml")
url = "https://optim.lightning.force.com/lightning/page/home"
driver.get(url)
time.sleep(2)
if not url == driver.current_url:
    driver.find_element(By.ID,'okta-signin-submit').click()
time.sleep(5)

# time element
# /html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/teamspirit-tslc-check-in-check-out-department-component/lightning-card/article/div[2]/slot/div[3]/div/div/table/tbody/tr[1]/td[4]
xpath = '//*[@id="brandBand_2"]/div/div/div/div/div/div/div[1]/div[1]/div[2]/article/div[2]/div/force-aloha-page/div/iframe'
frame = driver.find_element(By.XPATH, xpath)
driver.switch_to.frame(frame)
start_button = driver.find_element(By.ID,'btnStInput')
end_button = driver.find_element(By.ID, 'btnEtInput')
print(start_button)
send_click = False
if send_click and False:
    button.click()

driver.quit()
