# 4 отображение страницы товара
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("be@tester.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Very123Strong$%^Password78")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
shop_btn.click()
HTML_5_Forms = driver.find_element_by_css_selector(".products>li:nth-child(3)>a:nth-child(1)")
HTML_5_Forms.click()
HTML_5_Forms_title = driver.find_element_by_class_name("product_title")
HTML_5_Forms_title_text = HTML_5_Forms_title.text
if HTML_5_Forms_title_text == "HTML5 Forms":
    print("Заголовок книги называется: ", HTML_5_Forms_title_text)
else:
    print("Заголовок такой: ", HTML_5_Forms_title_text)
driver.quit()

# 5 количество товаров в категории
from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("be@tester.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Very123Strong$%^Password78")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
shop_btn.click()
category_HTML = driver.find_element_by_css_selector(".cat-item-19>a")
category_HTML.click()
category_HTML_count = driver.find_elements_by_css_selector(".products>li")
if len(category_HTML_count) == 3:
    print("количество товаров в категории HTML: 3")
else:
    print("количество товаров в категории HTML:" + str(len(category_HTML_count)))
driver.quit()

# 6 сортировка товаров
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("be@tester.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Very123Strong$%^Password78")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
time.sleep(5)
shop_btn.click()
time.sleep(5)
sorting = driver.find_element_by_class_name("orderby")
select = Select(sorting)
default_select = driver.find_element_by_css_selector(".orderby>option:nth-child(1)")
default_select_checked = default_select.get_attribute("value")
if default_select_checked == "menu_order":
    print("сортировка по умолчанию")
else:
    print("сортировка не по умолчанию")
select.select_by_value("price-desc")
price_desk_select = driver.find_element_by_css_selector(".orderby>option:nth-child(6)")
price_desk_select_checked = price_desk_select.get_attribute("value")
price_desk_select_selected = price_desk_select.get_attribute("selected")
print("value: ", price_desk_select_selected)
if price_desk_select_checked == "price-desc":
    print("сортировка по цене от большего к меньшему")
else:
    print("неправильная сортировка")
if price_desk_select_selected is not None:
    print("Selected price desk")
else:
    print("no attribute")
driver.quit()

# 7 отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path = "C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
account_btn = driver.find_element_by_css_selector("#menu-item-50>a")
account_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys("be@tester.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Very123Strong$%^Password78")
login_btn = driver.find_element_by_name("login")
login_btn.click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
time.sleep(5)
shop_btn.click()
android_quick = driver.find_element_by_css_selector(".products>li:nth-child(1)>a:nth-child(1)")
android_quick.click()
past_price = driver.find_element_by_css_selector(".price>del>.woocommerce-Price-amount")
past_price_text = past_price.text
assert past_price_text == "₹600.00"
print(past_price_text)
new_price = driver.find_element_by_css_selector(".price>ins>.woocommerce-Price-amount")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
print(new_price_text)
book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images>a>img")))
book_cover.click()
close_book_cover = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "pp_close")))
close_book_cover.click()
driver.quit()

# 8 проверка цены в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
time.sleep(5)
shop_btn.click()
add_html5_webapp = driver.find_element_by_css_selector(".products>li:nth-child(4)>a:nth-child(2)")
add_html5_webapp.click()
time.sleep(7)
item_amount = driver.find_element_by_class_name("cartcontents")
item_amount_text = item_amount.text
assert item_amount_text == "1 Item"
item_price = driver.find_element_by_css_selector(".wpmenucart-contents>.amount")
item_price_text = item_price.text
assert item_price_text == "₹180.00"
shop_cart = driver.find_element_by_class_name("wpmenucart-contents")
shop_cart.click()
subtotal_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td>.amount"), "₹180.00"))
total_price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td>strong>.amount"), "₹"))
driver.quit()

# 9 работа в корзине
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
time.sleep(5)
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5_webapp = driver.find_element_by_css_selector(".products>li:nth-child(4)>a:nth-child(2)")
add_html5_webapp.click()
time.sleep(7)
add_js_data = driver.find_element_by_css_selector(".products>li:nth-child(5)>a:nth-child(2)")
add_js_data.click()
shop_cart = driver.find_element_by_class_name("wpmenucart-contents")
shop_cart.click()
time.sleep(7)
remove_first_book = driver.find_element_by_css_selector(".shop_table_responsive.cart>tbody>.cart_item:nth-child(1)>.product-remove>a")
remove_first_book.click()
remove_undo = driver.find_element_by_css_selector(".woocommerce-message>a")
remove_undo.click()
quantity_input = driver.find_element_by_css_selector(".shop_table_responsive.cart>tbody>.cart_item:nth-child(1)>.product-quantity>.quantity>input")
quantity_input.clear()
quantity_input.send_keys(3)
update_basket = driver.find_element_by_name("update_cart")
update_basket.click()
quantity_input_value = quantity_input.get_attribute("value")
print("value: ", quantity_input_value)
assert quantity_input_value == "3"
time.sleep(7)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()
apply_coupon_error = driver.find_element_by_css_selector(".woocommerce-error>li")
apply_coupon_error_text = apply_coupon_error.text
if apply_coupon_error_text == "Please enter a coupon code.":
    print("Возникло правильное сообщение")
else:
    print("Сообщение: ", apply_coupon_error_text)
driver.quit()

# 10 покупка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a")
time.sleep(5)
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
add_html5_webapp = driver.find_element_by_css_selector(".products>li:nth-child(4)>a:nth-child(2)")
add_html5_webapp.click()
time.sleep(7)
shop_cart = driver.find_element_by_class_name("wpmenucart-contents")
shop_cart.click()
driver.implicitly_wait(10)
proceed_to_checkout_btn = driver.find_element_by_css_selector(".wc-proceed-to-checkout>a")
proceed_to_checkout_btn.click()
billing_first_name = driver.find_element_by_id("billing_first_name")
billing_first_name.send_keys("Egor")
billing_last_name = driver.find_element_by_id("billing_last_name")
billing_last_name.send_keys("Douglas")
billing_email = driver.find_element_by_id("billing_email")
billing_email.send_keys("be@tester.ru")
billing_phone = driver.find_element_by_id("billing_phone")
billing_phone.send_keys("007")
billing_country_selector = driver.find_element_by_id("select2-chosen-1")
billing_country_selector.click()
billing_country = driver.find_element_by_id("s2id_autogen1_search")
billing_country.send_keys("Turkey")
billing_country_result = driver.find_element_by_css_selector("#select2-results-1>li>div>span")
billing_country_result.click()
billing_address = driver.find_element_by_name("billing_address_1")
billing_address.send_keys("Apple street")
billing_postcode = driver.find_element_by_name("billing_postcode")
billing_postcode.send_keys("1")
billing_city = driver.find_element_by_name("billing_city")
billing_city.send_keys("2")
billing_province_sellector = driver.find_element_by_id("select2-chosen-2")
billing_province_sellector.click()
billing_province = driver.find_element_by_id("s2id_autogen2_search")
billing_province.send_keys("Antalya")
billing_province_result = driver.find_element_by_css_selector(".select2-result-label>span")
billing_province_result.click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(7)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
received_order = WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_method_result = WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table.order_details>tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()

