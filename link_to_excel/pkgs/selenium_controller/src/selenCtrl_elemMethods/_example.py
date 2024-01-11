import bs4

from selenium.webdriver.remote.webdriver import WebDriver

from ..seleniumControllerBase import unpack_loneChildTag_from_tag, Bs4HtmlElementNavigationError

def get_elem_example(
        driver: WebDriver
    ):
        post_tl_html = driver.page_source
        souped_html = bs4.BeautifulSoup(
            markup=post_tl_html, 
            features="html.parser"
        )
        target_elem = None
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
            target_elem =  lv17
        
        except IndexError:
            raise Bs4HtmlElementNavigationError()
        
        return target_elem