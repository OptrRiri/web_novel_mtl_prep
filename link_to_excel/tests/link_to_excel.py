import argparse

from ..vars import link_to_excel_test_vars

from ..src.novel_chapter_tl import NovelChapterTranslated
from ..src.write_to_excel import write_novelChapterTl_to_excel

def test():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", 
        "--link", 
        default=None
    )
    args = parser.parse_args()
    link = link_to_excel_test_vars.link if args.link == None else args.link
    tnc = NovelChapterTranslated()
    tnc.get_chapter_tl(
        chapter_link=link
    )
    tnc.log_chapter_tl()
    write_novelChapterTl_to_excel(
        novelChapterTl=tnc, 
        receiver_excel_filename=str(link_to_excel_test_vars.chapter_tl_receiver_xl_path), 
        set_headers=True
    )

if __name__ == "__main__":
    test()