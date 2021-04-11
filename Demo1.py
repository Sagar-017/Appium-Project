from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "platformVersion": "10",
  "deviceName": "eef9dcae"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
print("half done")
driver.find_element_by_id("com.google.android.googlequicksearchbox:id/hint_text_alignment").click()
