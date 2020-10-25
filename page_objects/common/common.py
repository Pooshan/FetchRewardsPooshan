from utils.logger import Logger

l = Logger()

class Common:
    """
    This class contains the methods that reusable irrespective of the website/application.
    """
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, strategy):
        """
        :param locator: locator value
        :param strategy: locator strategy example: xpath, id .. etc
        :return: web element
        """
        if strategy == "id":
            return self.driver.find_element_by_id(locator)
        elif strategy == "name":
            return self.driver.find_element_by_name(locator)
        elif strategy == "css_selector":
            return self.driver.find_element_by_css_selector(locator)
        elif strategy == "class_name":
            return self.driver.find_element_by_class_name(locator)
        elif strategy == "link_text":
            return self.driver.find_element_by_link_text(locator)
        elif strategy == "partial_link_text":
            return self.driver.find_element_by_partial_link_text(locator)
        elif strategy == "xpath":
            return self.driver.find_element_by_xpath(locator)
        else:
            raise RuntimeError("Please provide valid locator strategy")


    def click(self, locator, strategy):
        self.get_element(locator, strategy).click()
        l.log.info("Clicked on element {}".format(locator))

    def enter_text(self, locator, strategy, text):
        self.get_element(locator, strategy).send_keys(text)
        l.log.info("Text entered in this {}".format(locator))

