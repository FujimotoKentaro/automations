from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tenacity import retry, stop_after_delay, wait_fixed

# import chromedriver_binary
import time
import subprocess

port = 9222
p = subprocess.run(["open","-a","/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                    "--args",
                    "--new-window",
                    f"--remote-debugging-port={port}"])
# time.sleep(5)
options = Options()
options.add_experimental_option("debuggerAddress",f"127.0.0.1:{port}")
options.add_argument("--user-data-dir=" + "/Users/opm005789/Library/Application Support/Google/Chrome/Default")
options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(options=options)
# driver.execute_script("window.open();")

# teamspiritのリンク
# driver.get("https://optimcorporation.okta.com/app/salesforce/exk1hk8n5ic3Jj2XT0h8/sso/saml")
url = "https://optim.lightning.force.com/lightning/page/home"
driver.get(url)
wait = WebDriverWait(driver,15)

@retry(stop=stop_after_delay(10),wait=wait_fixed(1))
def find_element(by,name):
    return driver.find_element(by,name)
    raise Exception('retry error')

time.sleep(1)
if not url == driver.current_url:
    find_element(By.ID,'okta-signin-submit').click()
    print('signup')



# time element
# /html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/teamspirit-tslc-check-in-check-out-department-component/lightning-card/article/div[2]/slot/div[3]/div/div/table/tbody/tr[1]/td[4]

#  出勤状況を確認するパス
xpath = '//*[@id="brandBand_2"]/div/div/div/div/div/div/div[1]/div[1]/div[3]/teamspirit-tslc-check-in-check-out-department-component/lightning-card/article/div[2]/slot/div[3]/div/div/table/tbody/tr[1]/td[4]'
logged_time_element = find_element(By.XPATH, xpath)
logged_time = logged_time_element.text
print(logged_time)



#  teamspiritの出勤退勤ボタンのパス 出勤退勤ボタンが押せるようにフレームに移動している状態
frame_xpath = '//*[@id="brandBand_2"]/div/div/div/div/div/div/div[1]/div[1]/div[2]/article/div[2]/div/force-aloha-page/div/iframe'
frame = find_element(By.XPATH, frame_xpath)
driver.switch_to.frame(frame)

time.sleep(2)

#出勤状況を確認して出勤ボタンを押すか退勤ボタンを押すかを判定する
start_button = find_element(By.ID,'btnStInput')
end_button = find_element(By.ID, 'btnEtInput')
can_click = True
if not logged_time and can_click:
    print('NULL')
    start_button.click()

    print("出勤打刻をしました")
    print(start_button)
elif can_click:
    print('文字あり')
    end_button.click()
    # tmp_element = WebDriverWait(driver,10).until(
    #     expected_conditions.presence_of_element_located((By.ID, 'btnEtInput'))
    # )
    # tmp_element.click()
    # driver.find_element(By.XPATH,'//*[@id="btnEtInput"]').click()
    print("退勤打刻をしました")
    print(end_button)

driver.switch_to.default_content()

driver.quit()
