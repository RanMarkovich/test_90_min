import os

from pytest import fixture, mark
from selenium import webdriver


@fixture
def driver():
    driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'chromedriver'))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@fixture
def home_page(driver):
    from ui_tests.pages.home_page import HomePage
    return HomePage(driver)


@fixture
def arsenal_page(driver):
    from ui_tests.pages.arsenal_page import ArsenalPage
    return ArsenalPage(driver)


@fixture
def test_data():
    from ui_tests.resources.test_data import TestData
    return TestData()


@fixture
def locators():
    from ui_tests.resources.locators import Locators
    return Locators()


def test_header_links(home_page):
    home_page.are_all_links_in_header_menu()


def test_all_links_are_presented_in_premier_league(home_page):
    num_of_links = home_page.get_number_of_links_from_premier_league_drop_down()
    assert len(num_of_links) == 21, \
        f"failed to get 21 links in header premier league drop down, instead got: {len(num_of_links)}"


def test_change_site_lang(home_page, test_data):
    home_page.change_site_lang("es")
    home_page.assert_current_url(test_data.HOME_PAGE_SPANISH_URL)


@mark.parametrize('social', ['facebook', 'twitter', 'instagram', 'youtube', 'posts.rss'])
def test_social_links_has_suitable_icons(home_page, test_data, social):
    if social == 'facebook':
        d_value = test_data.SVG_FACEBOOK_ICON
    elif social == 'twitter':
        d_value = test_data.SVG_TWITTER_ICON
    elif social == 'instagram':
        d_value = test_data.SVG_INSTAGRAM_ICON_A
    elif social == 'youtube':
        d_value = test_data.SVG_YOUTUBE_ICON
    elif social == 'posts.rss':
        d_value = test_data.SVG_RSS_ICON

    act_icon = home_page.get_social_links_svg_icon(social)
    assert act_icon == d_value, \
        f"failed to get same icon for: {social} social link, expected: {d_value}, instead got: {act_icon}"


def test_premier_league_color_on_mouse_hover(home_page, test_data):
    color = home_page.get_premier_league_color_on_mouse_hover()
    assert color == test_data.DROP_DOWN_RGB_COLOR_ON_MOUSE_HOVER


def test_redirection_to_arsenal_feed(home_page, test_data):
    home_page.choose_feed_from_premier_league_drop_down('Arsenal')
    home_page.assert_current_url(test_data.ARSENAL_PAGE_URL)


def test_all_posts_in_arsenal_page_have_valid_images(arsenal_page):
    images_src = arsenal_page.get_all_posts_images_in_page()
    for image_src in images_src:
        arsenal_page.image_request_validation(image_src)
