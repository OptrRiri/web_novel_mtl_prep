from ..src import novel_chapter
from ..vars import request_headers
from pprint import pprint

def test():
    novelChapter = novel_chapter.NovelChapter()
    novelChapter.get_novelChapter_from_link_syosetu(
        link=input("paste syosetu chapter link: "), 
        headers=request_headers.headers
    )

    pprint(novelChapter.__dict__)

if __name__ == "__main__":
    test()