from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.google.com.hk/?hl=zh-cn")
driver.find_element_by_id("lst-ib").click()
driver.find_element_by_id("lst-ib").clear()
driver.find_element_by_id("lst-ib").send_keys("hello world")
driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
driver.find_element_by_link_text(u"Hello World - 维基百科，自由的百科全书").click()

html = driver.page_source
driver.get_screenshot_as_file("E:/Workspace_Python/JSprider/img/ss.png")
driver.close()