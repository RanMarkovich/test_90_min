from ui_tests.pages.base_page import BasePage
from ui_tests.resources.locators import Locators
from ui_tests.resources.test_data import TestData


class ArsenalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.ARSENAL_PAGE_URL)

    def get_all_posts_images_in_page(self) -> list:
        posts = self.driver.find_elements(*Locators.POSTS_IMAGES_LOCATORS)
        images = []
        for post in posts:
            images.append(post.get_attribute('src'))
        return images
