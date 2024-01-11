import time, winsound
from ..src import selenium_translator
from selenium.webdriver.common.by import By
from pprint import pprint
from ..vars import selenium_configs

def test(): 
    sc = selenium_translator.SeleniumTranslator()
    sc.driver = sc.get_driver_simple()
    sc.driver.get(
        url=selenium_configs.gtl_link
    )
    pprint(sc.driver.find_elements(
        by=By.TAG_NAME, 
        value="textarea"
    ))
    sc.driver.quit()

if __name__ == "__main__":
    test()