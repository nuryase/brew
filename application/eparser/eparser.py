import bs4 as bs
import urllib.request


class Parser:
    """
    Parses .xhtml files into plain text.
    """

    def __init__(self, chapters: list, path: str):
        self.chapters = chapters
        self.path = path

    def parse_xhtml(self):
        """
        Parses .xhtml files in OEBPS folder and places text into a dictionary. (chapter_number : chapter_content)

        Returns:
            ebook - A dictionary containing a key:value of chapter_number : chapter_content (Dict.)

                **Access using CHAPTER CONTENTS = ebook[CHAPTER NUMBER]
                e.g. chapter_one = ebook[1]
        """
        ebook = dict()
        chapter_number = 1

        for filename in self.chapters:
            source = urllib.request.urlopen(
                "file://" + self.path + "OEBPS/" + filename
            ).read()
            soup = bs.BeautifulSoup(source, "xml")
            chapter_text = ""
            for paragraph in soup.find_all("p"):
                chapter_text += str(paragraph.string) + "\n" + "\n"

            ebook[chapter_number] = chapter_text
            chapter_number += 1

        return ebook
