from ..src import selenium_translator

def test():
    driver = selenium_translator.SeleniumTranslator().get_driver_simple()
    driver.get("https://www.google.com")
    #driver.quit()

if __name__ == "__main__":
    test()