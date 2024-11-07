from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--no-sandbox")
s = Service('C:\\Users\\Lev\\PycharmProjects\\Python_SELENIUM\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

# CREDENTIALS
login = 'standard_user'
passwords = 'secret_sauce'
first_name = 'Test'
last_name = 'Testov'
zip_code = '2517'

# ПЕРЕХОД НА НУЖНУЮ СТРАНИЦУ И ОТКРЫТИЕ БРАУЗЕРА В МАКСИМАЛЬНОМ РАЗМЕРЕ
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print('Открыта страница авторизации')
time.sleep(2)

# ПОИСК ЛОКАТОРА ПОЛЯ ВВОДА ЛОГИНА И ВВОД
login_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
login_input.send_keys(login)
print('Введён логин')
time.sleep(2)

# ПОИСК ЛОКАТОРА ПОЛЯ ВВОДА ПАРОЛЯ И ВВОД
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
password_input.send_keys(passwords)
print('Введён пароль')
time.sleep(2)

# ПОИСК ЛОКАТОРА КНОПКИ АВТОРИЗАЦИИ И НАЖАТИЕ
auth_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
auth_button.click()
print('Нажата кнопка авторизации')
time.sleep(2)

# ПРОВЕРКА КОРРЕКТНОСТИ АВТОРИЗАЦИИ (ПО ВИДИМОСТИ ФИЛЬТРА И НАДПИСИ PRODUCTS)
filter_check = driver.find_element(By.XPATH, "//span[@data-test='active-option']")
product_check = driver.find_element(By.XPATH, "//span[@data-test='title']")
assert filter_check.text == 'Name (A to Z)' and product_check.text == 'Products'
print('Авторизация успешна✔️')
time.sleep(3)

# СКРОЛЛ ЭКРАНА ВНИЗ НА 300 ПИКСЕЛЕЙ
driver.execute_script("window.scrollBy(0, 300)")
action_1 = ActionChains(driver)
print('Скролл страницы⬇️')
time.sleep(2)

# ПОИСК НАЗВАНИЯ И ЦЕНЫ ПЕРВОГО ТОВАРА, СОХРАНЕНИЕ ИХ В ПЕРЕМЕННЫЕ И ДОБАВЛЕНИЕ В КОРЗИНУ
title_item_1 = driver.find_element(By.XPATH, "//a[@id='item_5_title_link']")
value_item_1 = title_item_1.text

price_item_1 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-price'])[4]")
value_price_item_1 = price_item_1.text.replace('$', '')

item_1_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
item_1_to_cart.click()
print('Первый товар добавлен в корзину🛍️')
time.sleep(2)

# ПОИСК НАЗВАНИЯ И ЦЕНЫ ВТОРОГО ТОВАРА, СОХРАНЕНИЕ ИХ В ПЕРЕМЕННЫЕ И ДОБАВЛЕНИЕ В КОРЗИНУ
title_item_2 = driver.find_element(By.XPATH, "//a[@id='item_3_title_link']")
value_item_2 = title_item_2.text

price_item_2 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-price'])[6]")
value_price_item_2 = price_item_2.text.replace('$', '')

item_2_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
item_2_to_cart.click()
print('Второй товар добавлен в корзину🛍️')
time.sleep(2)

# СКРОЛЛ ЭКРАНА В САМЫЙ ВЕРХ (0, 0)
driver.execute_script("window.scrollBy(0, -300)")
action_2 = ActionChains(driver)
print('Скролл страницы вверх⬆️')
time.sleep(3)

# ПОИСК ЛОКАТОРА И ПЕРЕХОД В КОРЗИНУ
cart = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cart.click()
print('Переход в корзину🛒')
time.sleep(2)

# ПРОВЕРКА ПЕРЕХОДА В КОРЗИНУ
cart_check = driver.find_element(By.XPATH, "//span[contains(text(), 'Your Cart')]")
assert cart_check.text == 'Your Cart'
print('Успешный переход в корзину✔️')
time.sleep(2)

# ПОИСК ЛОКАТОРА И ПЕРЕХОД НА СТРАНИЦУ ОПЛАТЫ
checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print('Переход на страницу оплаты')
time.sleep(2)

# ПОИСК ЛОКАТОРОВ И ЗАПОЛНЕНИЕ ПОЛЕЙ ИНФЫ ПО ДОСТАВКЕ
name_input = driver.find_element(By.XPATH, "//input[@id='first-name']")
name_input.send_keys(first_name)
print('Введено имя')
time.sleep(2)

last_name_input = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name_input.send_keys(last_name)
print('Введена фамилия')
time.sleep(2)

zip_code_input = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_code_input.send_keys(zip_code)
print('Введён ZIP')
time.sleep(2)

# ПОИСК ЛОКАТОРА И НАЖАТИЕ КНОПКИ CONTINUE
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print('Переход в Checkout')
time.sleep(2)

# СРАВНЕНИЕ НАИМЕНОВАНИЙ ТОВАРОВ В КОРЗИНЕ
checkout_title_item_1 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-name'])[1]")
checkout_title_item_2 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-name'])[2]")

assert value_item_1 == checkout_title_item_1.text and value_item_2 == checkout_title_item_2.text
print('Наименования товаров совпадают✔️')
time.sleep(2)

# СРАВНЕНИЕ ЦЕН ТОВАРОВ В КОРЗИНЕ
checkout_price_item_1 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-price'])[1]")
value_checkout_price_item_1 = checkout_price_item_1.text.replace('$', '')

checkout_price_item_2 = driver.find_element(By.XPATH, "(//div[@data-test='inventory-item-price'])[2]")
value_checkout_price_item_2 = checkout_price_item_2.text.replace('$', '')

assert value_price_item_1 == value_checkout_price_item_1 and value_price_item_2 == value_checkout_price_item_2
print('Цены товаров совпадают✔️')
time.sleep(2)

# ПРОВЕРКА КОРРЕКТНОСТИ СУММЫ ЗАКАЗА
assert float(value_price_item_1) + float(value_price_item_2) == float(value_checkout_price_item_1) + float(
    value_checkout_price_item_2)
print('Сумма корзины посчитана верно✔️')
time.sleep(2)

# НАЖАТИЕ КНОПКИ FINISH
driver.execute_script("window.scrollBy(0, 500)")
action = ActionChains(driver)
time.sleep(1)
finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
finish_button.click()
print('Нажата кнопка FINISH')
time.sleep(2)

# ПРОВЕРКА УСПЕШНОГО ОФОРМЛЕНИЯ ЗАКАЗА
result = driver.find_element(By.XPATH, "//h2[@data-test='complete-header']")
assert result.text == 'Thank you for your order!'
print('Заказ успешно создан✔️')
time.sleep(2)

# ЗАКРЫТИЕ БРАУЗЕРА
print('Тест завершён успешно, я молодец🥳🎉')
driver.quit()
print('Браузер закрыт✔️')
