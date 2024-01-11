import os
from pathlib import Path

FOLDER_OF_THIS_FILE = Path(
    os.path.dirname(
        p=os.path.realpath(
            path=__file__
        )
    )
)

tl_error_log_path = FOLDER_OF_THIS_FILE.parent / Path("logs") / Path("tl_error_log.json")
chapter_tl_log_path = FOLDER_OF_THIS_FILE.parent / Path("logs") / Path("chapter_tl_log.json")