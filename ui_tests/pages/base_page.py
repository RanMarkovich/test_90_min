import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def assert_element_is_displayed(self, by_locator):
        web_el = self.wait.until(EC.visibility_of_element_located(by_locator))
        assert web_el.is_displayed(), f"unable to locate element: {by_locator}"

    def hover_element(self, element: WebElement):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def scroll_to_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def assert_current_url(self, exp_url: str):
        assert self.driver.current_url == exp_url, \
            f"failed to get expected page url: {exp_url}, instead got: {self.driver.current_url}"

    @staticmethod
    def drop_down_selection_by_visible_text(element: WebElement, text: str):
        select = Select(element)
        select.select_by_visible_text(text)

    @staticmethod
    def get_element_color(element: WebElement):
        color = element.value_of_css_property('color')
        return color

    @staticmethod
    def image_request_validation(src: str):
        r = requests.get(src)
        assert r.status_code == 200, \
            f"failed to validate image request of src: {src}, expected s.code 200, " \
            f"instead got: {r.status_code} with message: {r.text}"
