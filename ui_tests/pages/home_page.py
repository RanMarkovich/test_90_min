from ui_tests.pages.base_page import BasePage
from ui_tests.resources.locators import Locators
from ui_tests.resources.test_data import TestData


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.HOME_PAGE_URL)

    def are_all_links_in_header_menu(self):
        for i in TestData.HOME_PAGE_EXPECTED_HEADERS_LINKS:
            header_menu_link_locator = Locators().get_header_menu_link_locator_by_xpath(i)
            self.assert_element_is_displayed(header_menu_link_locator)

    def get_number_of_links_from_premier_league_drop_down(self):
        self.open_premier_league_drop_down()
        premier_league_drop_down_list = self.driver.find_elements(*Locators.PREMIER_LEAGUE_DROP_DOWN_GRID_LOCATOR)
        return premier_league_drop_down_list

    def change_site_lang(self, lang: str):
        self.driver.find_element(*Locators.EDITIONS_BUTTON_LOCATOR).click()
        self.driver.find_element(*Locators().get_edition_button_locator_by_language(lang)).click()

    def get_social_links_svg_icon(self, partial_link_text: str):
        follow_up_title = self.driver.find_element(*Locators.FOLLOW_US_TITLE_LOCATOR)
        self.scroll_to_element(follow_up_title)
        social_list = self.driver.find_element(*Locators().get_social_link_icon_locator(partial_link_text))
        svg_icon = social_list.get_attribute('d')
        return svg_icon

    def get_premier_league_color_on_mouse_hover(self):
        premier_league = self.driver.find_element(*Locators().get_header_menu_link_locator_by_xpath('Premier League'))
        self.hover_element(premier_league)
        premier_league_hovered = self.driver.find_element(*Locators.PREMIER_LEAGUE_DROP_DOWN_LOCATOR)
        color = self.get_element_color(premier_league_hovered)
        return color

    def open_premier_league_drop_down(self):
        premier_league = self.driver.find_element(*Locators().get_header_menu_link_locator_by_xpath('Premier League'))
        self.hover_element(premier_league)

    def choose_feed_from_premier_league_drop_down(self, name: str):
        self.open_premier_league_drop_down()
        self.driver.find_element(*Locators().get_feed_from_drop_down_locator(name)).click()
