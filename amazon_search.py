import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AmazonSearch(object):

    CHROME_DRIVER = "/Users/argadeda/python-projects/python-selenium/driver/chromedriver"
    SEARCH_BAR = "twotabsearchtextbox"
    SEARCH_BUTTON = "//*[@id='nav-search-submit-button']"
    URL = "https://www.amazon.in/"

    def __init__(self, items):
        self.URL = AmazonSearch.URL
        self.items = items

        self.profile = webdriver.Chrome
        self.options = Options()
        self.driver = webdriver.Chrome(AmazonSearch.CHROME_DRIVER)

        self.driver.get(self.URL)
        self.driver.maximize_window()

    def search_items(self):

        for item in self.items:

            search_input = self.driver.find_element_by_id(AmazonSearch.SEARCH_BAR)
            search_input.clear()
            search_input.send_keys(item)
            time.sleep(2)
            search_button = self.driver.find_element_by_xpath(AmazonSearch.SEARCH_BUTTON)
            search_button.click()
            time.sleep(2)

    def tear_down(self):
        self.driver.close()


if __name__ == '__main__':

    amazon_search = AmazonSearch(["coffee", "notebook", "laptop"])
    amazon_search.search_items()
    amazon_search.tear_down()




