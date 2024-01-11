import os
from pathlib import Path

link = "https://ncode.syosetu.com/n8626im/75/"

FOLDER_OF_THIS_FILE = Path(
    os.path.dirname(
        p=os.path.realpath(
            path=__file__
        )
    )
)

chapter_tl_receiver_xl_path = FOLDER_OF_THIS_FILE.parent / Path("logs") / Path("chapter_tl_receiver.xlsx")