import requests, bs4
from ..vars import request_headers

class UnexpectedLinkError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NovelChapter:
    def __init__(self) -> None:
        self.chapter_subtitle: str = None
        self.chapter_preface: list[str] = None
        self.chapter_honbun: list[str] = None
        self.chapter_afterword: list[str] = None

    def get_novelChapter_from_link(
        self, 
        link: str
    ):
        for key in site_keyword_and_method_dict:
            if key in link:
                site_keyword_and_method_dict[key](
                    self=self, 
                    link=link, 
                    headers=request_headers.headers
                )
                break
        else:
            raise UnexpectedLinkError()

    def get_novelChapter_from_link_syosetu(
        self, 
        link: str, 
        headers: dict
    ):
        res = requests.get(
            url=link, 
            headers=headers
        )
        res.raise_for_status()
        souped_res = bs4.BeautifulSoup(
            markup=res.text, 
            features='html.parser'
        )
        
        novel_subtitle_elem = souped_res.select(
            selector='p[class="novel_subtitle"]'
        )[0]
        self.chapter_subtitle = novel_subtitle_elem.text

        novel_preface_elems = souped_res.select(
            selector='div[id="novel_p"]'
        )
        if novel_preface_elems != []:
            self.chapter_preface = [para_elem.text for para_elem in novel_preface_elems[0].children]
        
        novel_honbun_elem = souped_res.select(
            selector='div[id="novel_honbun"]'
        )[0]
        self.chapter_honbun = [para_elem.text for para_elem in novel_honbun_elem.children]

        novel_afterword_elems =  souped_res.select(
            selector='div[id="novel_a"]'
        )
        if novel_afterword_elems != []:
            self.chapter_afterword = [para_elem.text for para_elem in novel_afterword_elems[0].children]

    def get_novelChapter_from_link_kakuyomu(
        self, 
        link: str, 
        headers: dict
    ):
        res = requests.get(
            url=link, 
            headers=headers
        )
        res.raise_for_status()
        souped_res = bs4.BeautifulSoup(
            markup=res.text, 
            features='html.parser'
        )
        
        novel_subtitle_elem = souped_res.select(
            selector='p[class="widget-episodeTitle js-vertical-composition-item"]'
        )[0]
        self.chapter_subtitle: str = novel_subtitle_elem.text
        
        novel_honbun_elem = souped_res.select(
            selector='div[class="widget-episodeBody js-episode-body"]'
        )[0]
        self.chapter_honbun = [elem.text for elem in novel_honbun_elem.children]

site_keyword_and_method_dict = {
    "kakuyomu": NovelChapter.get_novelChapter_from_link_kakuyomu, 
    "syosetu": NovelChapter.get_novelChapter_from_link_syosetu
}