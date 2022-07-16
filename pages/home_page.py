from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import Page


driver = webdriver.Chrome(executable_path='/Users/rajni/PycharmProjects/GetTop_Project/chromedriver4')
driver.maximize_window()

driver.get('https://gettop.us/')


 #class HomePage(Page):

    # ORDERS_LINK = (By.CSS_SELECTOR, 'a#nav-orders.nav-a.nav-a-2.nav-progressive-attribute')

    # def open_homepage(self):
        # self.open_page('https://gettop.us/')


# def open_home_page(self):
   # self.open_page()


# def hover_over_mac(self):
  #  actions = ActionChains(self.driver)
  #  mac = self.find_element(*self.MAC)
  #  actions.move_to_element(mac)
   # actions.perform()