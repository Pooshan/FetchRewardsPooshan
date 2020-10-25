import time

from page_objects.common.common import Common

class Home(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_bar = '//input[@data-testid="search_input"]'
    search_button = '//button[@data-testid="facebar_search_button"]'
    fetch_rewards_search_result = 'Fetch Rewards'
    like_button = "//button[contains (@class, 'likeButton')]"

    def search_and_click(self, input_text):
        self.enter_text(Home.search_bar, "xpath", input_text)
        self.click(Home.search_button, "xpath")
        time.sleep(5)

    def open_fetch_rewards_and_like(self):
        self.click(Home.fetch_rewards_search_result, "link_text")
        time.sleep(5)
        self.click(Home.like_button, "xpath")

