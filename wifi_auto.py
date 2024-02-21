from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from subprocess import check_output


login = {
    "mvhstl": "mv@22",
    "grlhstl": "ctae123",
    "guest": "12345",
    "nscb": "nscb@22"
}

URL = "http://192.168.12.2:8090/"

wifi_list = ['TP-Link_2.4GHz_5E40DB', 'mvtp', 'mv', 'MVCTAE', 'mvhstl118', 'mvhstl', 'mvhostel', 'mvhstl132']


def get_connected_wifi_id():
    command = ["netsh", "wlan", "show", "interfaces"]
    output = check_output(command)
    data = output.decode("utf-8")
    for line in data.splitlines():
        if "SSID" in line:
            return line.split(":")[-1].strip()
    return None


def connect():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # Bug tab sleeps
    driver = webdriver.Chrome(options=chrome_options)
    # driver.set_window_position(0, -1000)
    # to be tested
    driver.get(URL)
    is_true = True
    while is_true:
        for username, password in login.items():
            Username = driver.find_element(By.NAME, value="username")
            Username.send_keys(username)
            Password = driver.find_element(By.NAME, value="password")
            Password.send_keys(password)
            submit = driver.find_element(By.NAME,"btnSubmit")
            submit.click()
            sleep(1)
            status = driver.find_element(By.XPATH, '/html/body/form/div[1]/div[2]').text.split("\n")[0]
            if status == "You have successfully logged in":
                is_true = False
                break
            else:
                Username.clear()
                Password.clear()


current = get_connected_wifi_id()
for wifi in wifi_list:
    if current == wifi:
        connect()
        break
