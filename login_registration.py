# 2 регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
reg_email_field = driver.find_element_by_id("reg_email")
reg_email_field.send_keys("be@tester.ru")
reg_password_field = driver.find_element_by_id("reg_password")
reg_password_field.send_keys("Very123Strong$%^Password78")
register_btn = driver.find_element_by_name("register")
register_btn.click()

# 3 логин в систему
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("be@tester.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Very123Strong$%^Password78")
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout_btn = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation>ul>li:nth-child(6)>a")
logout_btn_text = logout_btn.text
print(logout_btn_text)
if logout_btn_text == "Logout":
    print("есть logout")
else:
    print("нет logout")
driver.quit()