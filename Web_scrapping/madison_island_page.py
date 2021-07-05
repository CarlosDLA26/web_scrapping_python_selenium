from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

class MadisonIslandPage():
    """Class to interact with web page Madison Island"""

    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://demo.onestepcheckout.com/' 

    @property
    def is_loaded(self):
        """ Check if a web site's page is loaded
        
        Parameters
        ----------
        No parameters

        Returns 
        -------
        Boolean
        """
        WebDriverWait(self._driver, 15).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    @property
    def keyword(self):
        """
        Returns
        -------
        String
            string with value of the search field
        """
        return self._driver.find_element_by_name('q').get_attribute('value')

    def open_principal_page(self):
        self._driver.get(self._url)

    def search_click(self):
        self._driver.find_element_by_name('q').submit()
    
    def type_search(self, keyword):
        search_field = self._driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(keyword)

    def search(self, keyword):
        """Type and submit a search in web page's search field

        Parameters
        ----------
        keyword : string
            keyword to perform the search
        """
        self.type_search(keyword)
        self.search_click()

    def web_scrapping_products(self):
        """ Perform web scrapping of a search, 
            complement this function with 'search(keyword)'
        
        Parameters
        ----------
        No parameters

        Returns 
        -------
        Dictionary
            returns dictionary with:
            key:   name of product
            value: price of product
        """
        driver = self._driver
        message_search = None
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/header/div/a/img[1]')))
        
        try :
            products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
            prices   = driver.find_elements_by_xpath('//span[@class="price"]')
            return {products[i].text:prices[i].text for i in range(len(products))}
        except:
            return {} 