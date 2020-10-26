from page_objects.others.home import Home
from page_objects.others.login import Login


class TestLikeFetchRewardsPage:

    def test_like_fetch_rewards_page(self, driver):
        login = Login(driver)
        home = Home(driver)
        login.login("fetchrewardscoding@gmail.com", "fetchrewards24")
        home.search_and_click("Fetch Rewards")
        home.open_fetch_rewards_and_like()
