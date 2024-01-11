import time, winsound
from ..src import selenium_translator
from selenium.webdriver.common.by import By
from pprint import pprint
from ..vars import selenium_configs

def test(): 
    sc = selenium_translator.SeleniumTranslator()
    sc.driver = sc.get_driver_simple()
    sc.open_gtl(
        driver=sc.driver
    )
    input_elem = sc.get_gtl_input_elem(
        driver=sc.driver
    )
    input_elem.click()
    input_elem.send_keys("なんで")
    time.sleep(3)
    pprint(
        sc.get_gtl_output_elem_navBs4(
            driver=sc.driver
        )
    )
    sc.driver.quit()

if __name__ == "__main__":
    test()