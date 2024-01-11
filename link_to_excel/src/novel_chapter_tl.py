import datetime

from . import raw_tl_pair
from ..vars import skip_tl, log_paths

from pprint import pprint

from .novel_chapter import NovelChapter
from .selenium_translator import SeleniumTranslator
from ..pkgs.json_handler.src.handler import JsonHandler

class NovelChapterTranslated(NovelChapter):
    def __init__(
        self
    ) -> None:
        super().__init__()
        self.chapter_subtitle_tlPair: raw_tl_pair.RawTlPair = None
        self.chapter_preface_tlPairs: list[raw_tl_pair.RawTlPair] = None
        self.chapter_honbun_tlPairs: list[raw_tl_pair.RawTlPair] = None
        self.chapter_afterword_tlPairs: list[raw_tl_pair.RawTlPair | None] = None

    def get_chapter_tl(
        self,
        chapter_link: str
    ):
        self.get_novelChapter_from_link(
            link=chapter_link
        )
        self.seleniumTranslator = SeleniumTranslator()
        self.seleniumTranslator.driver = self.seleniumTranslator.get_driver_simple()
        self.seleniumTranslator.open_gtl(
            driver=self.seleniumTranslator.driver
        )

        self.chapter_subtitle_tlPair = raw_tl_pair.RawTlPair(
            raw=self.chapter_subtitle, 
            tl=self.seleniumTranslator.get_translation(
                driver=self.seleniumTranslator.driver, 
                text=self.chapter_subtitle
            )
        )

        self.chapter_honbun_tlPairs = []
        for para in self.chapter_honbun:
            if para in skip_tl.blacklist:
                rtp = raw_tl_pair.RawTlPair(
                    raw=para, 
                    tl=None
                )
                self.chapter_honbun_tlPairs.append(rtp)
                continue

            rtp = raw_tl_pair.RawTlPair(
                raw=para, 
                tl=self.seleniumTranslator.get_translation(
                    driver=self.seleniumTranslator.driver, 
                    text=para
                )
            )
            self.chapter_honbun_tlPairs.append(rtp)
            pprint(
                {
                    "raw": rtp.raw, 
                    "tl": rtp.tl
                }
            )
        
        if self.chapter_preface != None:
            self.chapter_preface_tlPairs = []
            for para in self.chapter_preface:
                if para in skip_tl.blacklist:
                    rtp = raw_tl_pair.RawTlPair(
                        raw=para, 
                        tl=None
                    )
                    self.chapter_preface_tlPairs.append(rtp)
                    continue
                rtp = raw_tl_pair.RawTlPair(
                        raw=para, 
                        tl=self.seleniumTranslator.get_translation(
                            driver=self.seleniumTranslator.driver, 
                            text=para
                        )
                    )
                self.chapter_preface_tlPairs.append(rtp)
                pprint(
                    {
                        "raw": rtp.raw, 
                        "tl": rtp.tl
                    }
                )

        if self.chapter_afterword != None:
            self.chapter_afterword_tlPairs = []
            for para in self.chapter_afterword:
                if para in skip_tl.blacklist:
                    rtp = raw_tl_pair.RawTlPair(
                        raw=para, 
                        tl=None
                    )
                    self.chapter_afterword_tlPairs.append(rtp)
                    continue
                rtp = raw_tl_pair.RawTlPair(
                    raw=para, 
                    tl=self.seleniumTranslator.get_translation(
                        driver=self.seleniumTranslator.driver, 
                        text=para
                    )
                )
                self.chapter_afterword_tlPairs.append(rtp)
                pprint(
                    {
                        "raw": rtp.raw, 
                        "tl": rtp.tl
                    }
                )

        self.seleniumTranslator.driver.quit()
        
    def log_chapter_tl(self):
        jsonHandler = JsonHandler(log_path=log_paths.chapter_tl_log_path)
        existing_logs = jsonHandler.get_json_as_list(
            log_path=jsonHandler.log_path
        )
        new_log = {
            "time": str(datetime.datetime.now()), 
            "chapter_subtitle": self.chapter_subtitle, 
            "chapter_subtitle_tl": self.chapter_subtitle_tlPair.tl, 
            "chapter_preface": None if self.chapter_preface == None else [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in self.chapter_preface_tlPairs], 
            "chapter_honbun": [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in self.chapter_honbun_tlPairs], 
            "chapter_afterword": None if self.chapter_afterword == None else [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in self.chapter_afterword_tlPairs], 

        }
        log_obj = [new_log] + existing_logs
        jsonHandler.set_obj_as_json(
            log_path=jsonHandler.log_path, 
            obj=log_obj
        )