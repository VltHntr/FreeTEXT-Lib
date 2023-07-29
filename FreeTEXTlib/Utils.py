import json
import os
import datetime

from FreeTEXTlib.Models import Creator


class Formater:
    def __init__(self) -> None:
        self.format = {}
        self.isInit = False

    def init_format(self, creator: Creator):
        if self.isInit:
            print("Already init...")
        else:
            print("Init Formater...")
            form = [
                self.__init_header(creator),
                self.__init_body(),
                self.__init_footer()
            ]

            for i in form:
                self.format.update(i)

            print("Formatter is init.")

    def __init_header(self, creator: Creator):
        print("Init Header...")
        header = {
            "header": {
                "creator": {
                    "lastname": creator.get_lastname(),
                    "firstname": creator.get_firstname()
                },
                "date": datetime.date.today()
            }
        }
        print("Header is init.")

        return header

    def __init_body(self):
        print("init Body...")
        body = {"body": ""}
        print("Body is Init:")

        return body

    def __init_footer(self):
        print("Init footer...")
        footer = {
            "footer": {
                "libver": 0.1,
                "progver": 0.1,
                "fmtver": 0.1
            }
        }
        print("Footer is init.")

        return footer


class SaveManager:
    def __init__(self, basePath: str, formater: Formater = None) -> None:
        self.basePath = basePath
        self.formater = formater

        if not os.path.exists(self.basePath):
            os.makedirs(self.basePath)

    def save_to_text(self, fileName: str, content: str) -> None:
        with open(f"{self.basePath}/{fileName}.txt", "w") as f:
            f.write(content)

    def load_from_text(self, fileName: str) -> str:
        with open(f"{self.basePath}/{fileName}.txt", "r") as f:
            content = f.read()

        return content
