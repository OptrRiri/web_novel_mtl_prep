import json

from pathlib import Path

class JsonHandler:
    def __init__(
        self, 
        log_path: Path = None
    ) -> None:
        self.log_path: Path = log_path

    def get_json_as_list(self, log_path: Path):
        with open(
            file=str(log_path), 
            mode="r", 
            encoding="utf8"
        ) as json_file:
            log_as_list = json.load(fp=json_file)
            if type(log_as_list) != list:
                raise ValueError("json.load() does not return a list")
            return log_as_list
        
    def get_json_as_dict(self, log_path: Path):
        with open(
            file=str(log_path), 
            mode="r", 
            encoding="utf8"
        ) as json_file:
            log_as_list = json.load(fp=json_file)
            if type(log_as_list) != dict:
                raise ValueError("json.load() does not return a dict")
            return log_as_list
        
    def set_obj_as_json(
        self, 
        log_path: Path, 
        obj
    ): 
        with open(
            file=str(log_path), 
            mode="w", 
            encoding="utf8"
        ) as json_file:
            json.dump(
                obj=obj, 
                fp=json_file, 
                ensure_ascii=False, 
                indent=4
            )