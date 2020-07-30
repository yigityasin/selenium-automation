import os
import random
import sys
from time import sleep

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


def scrapper(search_term):
    host = "http://localhost:4444"
    driver = webdriver.Remote(
        command_executor=host + "/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME
    )

    node_socket = requests.get(host + "/grid/api/testsession?session=" + driver.session_id)
    robot_ip = node_socket.json()["proxyId"].replace(".", "-").split("//")[1].split(":")[0]

    df = pd.read_csv(robot_ip + ".csv") if os.path.exists(robot_ip + ".csv") else pd.DataFrame()

    driver.get("https://google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)

    sleep_duration = random.randint(1, 10)
    print(robot_ip + " sleeps " + str(sleep_duration) + " second(s).")
    sleep(sleep_duration)  # simulate long running automation

    results = driver.find_elements_by_css_selector("div.g")
    link = results[0].find_element_by_tag_name("a")
    href = link.get_attribute("href")
    print("Search term: " + search_term + "\nURL: " + href)
    df = df.append({"Search Term": search_term, "URL":href}, ignore_index=True)
    df.to_csv(robot_ip + ".csv", index=False)
    driver.quit()


if __name__ == "__main__":
    scrapper(sys.argv[1])
