from ..src import selenium_translator

def test():
    sc = selenium_translator.SeleniumTranslator()
    sc.driver = sc.get_driver_simple()
    sc.open_gtl(
        driver=sc.driver
    )
    tl = sc.get_translation(
        driver=sc.driver, 
        text="（え……えっと、確か汗で濡れた体を拭いてあげると嬉しいって……。そ、それに今の怜が一人でシャワーを浴びるのはまだ辛いだろうし……）"
    )
    print(tl)
    sc.driver.quit()

if __name__ == "__main__":
    test()