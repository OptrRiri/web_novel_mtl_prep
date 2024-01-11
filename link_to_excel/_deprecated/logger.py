import datetime
from pathlib import Path

from ..vars import log_paths

from ..pkgs.json_handler.src.handler import JsonHandler
from ..src.novel_chapter_tl import NovelChapterTranslated

class Logger(JsonHandler):
    def __init__(self, log_path: Path = None) -> None:
        super().__init__(log_path)
        self.tlError_log_path = log_paths.tl_error_log_path
        self.chapterTl_log_path = log_paths.chapter_tl_log_path
        
    '''def log_tlError(
        self, 
        trigger_text: str
    ):
        existing_logs = self.get_json_as_list(log_path=self.tlError_log_path)
        new_log = {
            "trigger_text": trigger_text,
            "time": datetime.datetime.now()
        }
        log_obj = [new_log] + existing_logs
        self.set_obj_as_json(
            log_path=self.tlError_log_path, 
            obj=log_obj
        )
'''
    '''def log_chapter_tl(
        self, 
        novelChapterTled: NovelChapterTranslated
    ):
        existing_logs = self.get_json_as_list(
            log_path=self.chapterTl_log_path
        )
        new_log = {
            "time": datetime.datetime.now(), 
            "chapter_subtitle": novelChapterTled.chapter_subtitle, 
            "chapter_subtitle_tl": novelChapterTled.chapter_subtitle_tlPair.tl, 
            "chapter_preface": None if novelChapterTled.chapter_preface == None else [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in novelChapterTled.chapter_preface_tlPairs], 
            "chapter_honbun": [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in novelChapterTled.chapter_honbun_tlPairs], 
            "chapter_afterword": None if novelChapterTled.chapter_afterword == None else [{
                "raw": pair.raw, 
                "tl": pair.tl
            } for pair in novelChapterTled.chapter_afterword_tlPairs], 

        }
        log_obj = [new_log] + existing_logs
        self.set_obj_as_json(
            log_path=self.chapterTl_log_path, 
            obj=log_obj
        )'''