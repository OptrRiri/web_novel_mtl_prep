import os, time, json, subprocess, sys, bs4, winsound, typing, datetime

from ..vars import selenium_configs, skip_tl, log_paths

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service
from tkinter import filedialog
from decimal import Decimal
from pprint import pprint

from ..pkgs.json_handler.src.handler import JsonHandler
from ..pkgs.selenium_controller.src.seleniumControllerBase import unpack_loneChildTag_from_tag, ControllerBase

class SeleniumTranslator(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.gtl_opened = None
        self.driver = None
        self.gecko_path_added = None
    
    def open_gtl(
        self, 
        driver: WebDriver
    ):
        self.open_page(
            driver=driver, 
            page_link=selenium_configs.gtl_link
        )
        self.gtl_opened = True

    def get_gtl_input_elem(
        self, 
        driver: WebDriver
    ):
        if self.gtl_opened != True:
            raise GtlNotOpenedError()
        
        text_input_elem = driver.find_elements(
            by=By.TAG_NAME, 
            value="textarea"
        )[0]
        return text_input_elem

    def get_gtl_output_elem_navBs4(
        self, 
        driver: WebDriver
    ):
        post_tl_html = driver.page_source
        souped_html = bs4.BeautifulSoup(
            markup=post_tl_html, 
            features="html.parser"
        )
        try:
            lv0_body_elem = souped_html.select(
                selector='body'
            )[0]
            lv1_cwiz_elem = [elem for elem in lv0_body_elem.children if isinstance(elem, bs4.Tag) and elem.name == "c-wiz"][0]
            lv2: bs4.Tag = unpack_loneChildTag_from_tag(lv1_cwiz_elem)
            lv3_div_elem: bs4.Tag = list(lv2.children)[1]
            lv4: bs4.Tag = unpack_loneChildTag_from_tag(lv3_div_elem)
            lv5_div_elem: bs4.Tag = list(lv4.children)[1]
            lv6: bs4.Tag = unpack_loneChildTag_from_tag(lv5_div_elem)
            lv7_div_elem: bs4.Tag = list(lv6.children)[1]
            lv8_div_elem: bs4.Tag = list(lv7_div_elem.children)[1]
            lv9_div_elem: bs4.Tag = list(lv8_div_elem.children)[-1]
            lv10_cwiz_elem: bs4.Tag = list(lv9_div_elem.children)[1]
            lv11_div_elem: bs4.Tag = list(lv10_cwiz_elem.children)[1]
            lv12_div_elem: bs4.Tag = list(lv11_div_elem.children)[-1]
            lv13: bs4.Tag = unpack_loneChildTag_from_tag(lv12_div_elem)
            lv14_div_elem: bs4.Tag = list(lv13.children)[0]
            lv15_span_div: bs4.Tag = list(lv14_div_elem.children)[0]
            lv16: bs4.Tag = unpack_loneChildTag_from_tag(lv15_span_div)
            lv17: bs4.Tag = unpack_loneChildTag_from_tag(lv16)
            return lv17
        
        except IndexError:
            raise TlResultTagNotFoundError()
        
    def get_translation(
        self, 
        driver: WebDriver, 
        text: str
    ):
        if self.gtl_opened != True: 
            raise GtlNotOpenedError()
        input_elem = self.get_gtl_input_elem(
            driver=driver
        )
        self.click_clear_type_elem(
            elem=input_elem, 
            type_this=text
        )
        time.sleep(selenium_configs.interval_wait_for_complete_tl)
        try:
            return self.get_gtl_output_elem_navBs4(
                driver=driver
            ).text
        except TlResultTagNotFoundError:
            self.log_tlError(trigger_text=text)
            raise CheckTlErrorLogError()
        
    def log_tlError(
        self, 
        trigger_text: str
    ):
        jsonHandler = JsonHandler(log_path=log_paths.tl_error_log_path)
        existing_logs = jsonHandler.get_json_as_list(log_path=jsonHandler.log_path)
        new_log = {
            "trigger_text": trigger_text,
            "time": str(datetime.datetime.now())
        }
        log_obj = [new_log] + existing_logs
        jsonHandler.set_obj_as_json(
            log_path=jsonHandler.log_path, 
            obj=log_obj
        )

class GtlNotOpenedError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TlResultTagNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CheckTlErrorLogError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)