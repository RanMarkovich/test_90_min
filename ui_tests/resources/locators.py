from selenium.webdriver.common.by import By


class Locators:
    # ===================== HomePage locators ===================== #
    HEADER_MENU_LINK_LOCATOR = (By.XPATH, "//li[contains(.,'<TEXT>')]")
    PREMIER_LEAGUE_DROP_DOWN_LOCATOR = (By.XPATH, "//span[contains(text(),'Premier League')]")
    PREMIER_LEAGUE_DROP_DOWN_GRID_LOCATOR = (By.CSS_SELECTOR, "a._1qaz7go")
    EDITIONS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div[aria-label='editions']")
    EDITION_DROP_DOWN_ITEM_LOCATOR = (By.CSS_SELECTOR, "a[href*='<LINK_TEXT>']")
    FOLLOW_US_TITLE_LOCATOR = (By.XPATH, "//h4[contains(.,'FOLLOW US')]")
    SVG_SOCIAL_ICON_LOCATOR = (By.CSS_SELECTOR, "a[href*='<PARTIAL_LINK>']<PATH>")
    FEED_FROM_DROP_DOWN_LOCATOR = (By.XPATH, "//span[contains(.,'<TEXT>')]")

    # ===================== ArsenalPage locators ===================== #
    POSTS_IMAGES_LOCATORS = (By.CSS_SELECTOR, "img.feedpage-article__thumbnail")

    def get_header_menu_link_locator_by_xpath(self, contains_text):
        header_menu_link = list(self.HEADER_MENU_LINK_LOCATOR)
        header_menu_link[1] = header_menu_link[1].replace('<TEXT>', contains_text)
        return header_menu_link[0], header_menu_link[1]

    def get_edition_button_locator_by_language(self, lang: str):
        edition_dd_btn_locator = list(self.EDITION_DROP_DOWN_ITEM_LOCATOR)
        if lang == "es":
            edition_dd_btn_locator[1] = edition_dd_btn_locator[1].replace('<LINK_TEXT>', '/es?')
        elif lang == "de":
            edition_dd_btn_locator[1] = edition_dd_btn_locator[1].replace('<LINK_TEXT>', '.de/?')
        return edition_dd_btn_locator[0], edition_dd_btn_locator[1]

    def get_social_link_icon_locator(self, partial_link_text: str):
        svg_social_icon_locator = list(self.SVG_SOCIAL_ICON_LOCATOR)
        if partial_link_text == 'facebook' or partial_link_text == 'instagram' or partial_link_text == 'youtube':
            svg_social_icon_locator[1] = svg_social_icon_locator[1].replace('<PATH>', '>div>svg>g>g>path')
        elif partial_link_text == 'twitter':
            svg_social_icon_locator[1] = svg_social_icon_locator[1].replace('<PATH>', '>div>svg>g>g>g>path')
        elif partial_link_text == 'posts.rss':
            svg_social_icon_locator[1] = svg_social_icon_locator[1].replace('<PATH>', '>div>svg>g>g>g>g>g>path')

        svg_social_icon_locator[1] = svg_social_icon_locator[1].replace('<PARTIAL_LINK>', partial_link_text)
        return svg_social_icon_locator[0], svg_social_icon_locator[1]

    def get_feed_from_drop_down_locator(self, text: str):
        feed_from_dd_locator = list(self.FEED_FROM_DROP_DOWN_LOCATOR)
        feed_from_dd_locator[1] = feed_from_dd_locator[1].replace('<TEXT>', text)
        return feed_from_dd_locator[0], feed_from_dd_locator[1]
