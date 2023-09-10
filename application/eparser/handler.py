import zipfile
import os


class EPUBHandler:
    """
    Unzips an EPUB file. An EPUB is an unencrypted zipped archive containing a set of resources.

    META-INF:
        Contains the [container.xml] file.

    OEBPS:
        Contains the .xhtml files container chapters, and other resources.

    Gets chapter contents from EPUB OEBPS folder.
    """

    def __init__(self, path: str, epub_name: str):
        self.path = path
        self.epub_name = epub_name

    def extract_epub(self):
        """
        Unzips and extracts epub contents into [epubs] directory.

        Parameters:
            epub_path - the epub file path. (String)
            name - name for the epub folder || user will use this name to select (String)
        """
        # Make new epub directory
        epub_directory = self.current_path()

        try:
            os.mkdir(epub_directory)
        except FileExistsError:
            print("ERROR: Directory already exists.")

        try:
            with zipfile.ZipFile(self.path, "r") as zip_ref:
                zip_ref.extractall(epub_directory)
        except FileNotFoundError:
            print("ERROR: File cannot be found.")

    def current_path(self):
        """
        Sets current path.
        """
        current_path = os.getcwd()
        return current_path + "/epubs/" + self.epub_name + "/"

    def get_chapters(self):
        """
        Finds all files ending with .xhtml and store them in list.
        """
        chapters = []
        epub_directory = self.current_path()
        for filename in sorted(os.listdir(epub_directory + "OEBPS/")):
            if filename.endswith("xhtml"):
                chapters.append(filename)

        return chapters
