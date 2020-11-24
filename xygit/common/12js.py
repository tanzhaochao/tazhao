from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://www.12306.cn/index/")

js = 'document.getElementById("train_date").removeAttribute("readonly"); document.getElementById("train_date").value="2020-11-09"'
driver.execute_script(js)