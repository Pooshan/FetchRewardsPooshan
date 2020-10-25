from page_objects.others.login import Login
import time

class TestLikeFetchRewardsPage:

    def test_like_fetch_rewards_page(self, driver):
        login = Login(driver)
        login.login("fetchrewardscoding@gmail.com", "fetchrewards24")
        time.sleep(10)
