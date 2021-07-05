from madison_island_page import MadisonIslandPage
from selenium import webdriver
from time import sleep
import unittest, json

def get_data(file_name):
    """ Get data of a text file

    Paramaters
    ----------
    file name : string
        text file's path with keywords to search

    Returns
    -------
    list
        list with keywords to search
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            words = [word.strip() for word in f]
        return words
    except FileNotFoundError:
        return []


def generate_json(data, file, indent=4):
    with open(file, 'w') as f:
        json.dump(data, f, indent=indent)


class WebScrapping(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('.\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()

    def test_madison_island(self):
        """Change this function to web automation"""
        keywords = get_data('words_search.txt')
        web_scrapping = {}
        madison_ip = MadisonIslandPage(self.driver)
        madison_ip.open_principal_page()

        for word in keywords:
            madison_ip.search(word)
            web_scrapping[word] = madison_ip.web_scrapping_products()

        generate_json(web_scrapping, 'json_files/test.json', 4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)