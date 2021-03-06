from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    def launch_driver(self, browser):
        _driver = None
        if browser.lower() == "chrome":
            chrome_options = webdriver.ChromeOptions()
            # To disable notification on Chrome
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            _driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = chrome_options)
        elif browser.lower() == "firefox":
            _driver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
        else:
            raise RuntimeError("{} browser is not supported yet".format(browser))
        return _driver

    def quit_driver(self, driver):
        driver.quit()

    def launch_url(self, driver, url):
        driver.get(url)
        driver.maximize_window()



