from pprint import pprint

from ..src.novel_chapter_tl import NovelChapterTranslated

def test():
    tnc = NovelChapterTranslated()
    tnc.get_chapter_tl(
        chapter_link="https://ncode.syosetu.com/n8626im/75/"
    )
    tnc.log_chapter_tl()
    
if __name__ == "__main__":
    test()