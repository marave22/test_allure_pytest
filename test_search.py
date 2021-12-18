# import time
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType

exec_path = "drivers/chromedriver.exe"


class TestProjectSearch:

    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        self.driver.quit()

    @allure.feature("Open Pages")
    @allure.story("Opens the Google page")
    @allure.severity("blocker")
    def test_google_search(self):
        self.driver.get("https://www.google.com/")
        with allure.step("Doing Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Google"

    @allure.feature("Open Pages")
    @allure.story("Opens the Yandex page")
    @allure.severity("critical")
    def test_yandex_search(self):
        self.driver.get("https://www.yandex.ru/")
        with allure.step("Doing Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Яндекс"

    @allure.feature("Open Pages")
    @allure.story("Opens the Yahoo page")
    @allure.severity("medium")
    def test_yahoo_search(self):
        self.driver.get("https://www.yahoo.com/")
        with allure.step("Doing Screenshot"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screen", attachment_type=AttachmentType.PNG)
        assert self.driver.title == "Yahoo | Mail, Weather, Search, Politics, News, Finance, Sports & Video"

