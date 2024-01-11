import bs4, time

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webelement import WebElement
from typing import Callable
from pprint import pprint

class ControllerBase:
    def __init__(self) -> None:
        self.driver = None

    def get_driver_simple(self):
        driver = webdriver.Firefox()
        return driver

    '''
    def get_driver_seleniumProfile(self):
        subprocess.Popen(
            args=selenium_configs.firefox_marionette_cmdStr, 
            shell=True, 
            cwd=str(
                Path(selenium_configs.firefox_binary_location).parent
            )
        )
        #print("created marionette")
        
        #print("trying to create driver")
        options = Options()
        options.binary_location = selenium_configs.firefox_binary_location
        options.add_argument(
            argument="-profile"
        )
        options.add_argument(
            argument=selenium_configs.firefox_profile_pathStr
        )
        service = Service(
            executable_path=selenium_configs.geckopath
        )
        service.service_args = selenium_configs.service_args
        #print("driver options and service created")
        
        winsound.Beep(400, 2000)
        driver = webdriver.Firefox(
            options=options, 
            service=service
        )
        #print("driver created")
        winsound.Beep(400, 2000)
        return driver
    '''
    
    def open_page(
        self, 
        driver: WebDriver, 
        page_link: str
    ):
        driver.get(
            url=page_link
        )

    def get_elem_from_page(
        self, 
        driver: WebDriver, 
        page_link: str, 
        elem_method: Callable[[WebDriver], bs4.Tag], 
        delay: int = 0
    ) -> bs4.Tag:
        self.open_page(
            driver=driver, 
            page_link=page_link
        )
        time.sleep(delay)
        return elem_method(
            driver=driver
        )
    
    def click_clear_type_elem(
        self, 
        elem: WebElement, 
        type_this: str
    ): 
        elem.click()
        elem.send_keys(Keys.CONTROL, "a")
        elem.send_keys(Keys.BACKSPACE)
        elem.send_keys(type_this)

class Bs4HtmlElementNavigationError(Exception): 
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def unpack_loneChildTag_from_tag(tag: bs4.Tag) -> bs4.Tag:
    return get_child_tags_from_tag(tag=tag)[0]

def get_child_tags_from_tag(tag: bs4.Tag):
    return [elem for elem in tag.children if type(elem) == bs4.Tag]