import json
import os
import datetime

from FreeTEXTlib.Models import Creator
from FreeTEXTlib.Models import DataForm, Header, Body, Footer, Creator


class Formatter:
    data: DataForm

    def __init__(self) -> None:
        self.format = {}
        self.isInit = False

    def init_format(self, creator: Creator):
        if self.isInit:
            print("Already initialize...")
        else:
            print("initialize Formatter...")

            self.data = DataForm(
                header=Header(
                    creator=creator
                ),
                body=Body(body="")
            )

            print("Formatter is initialize.")
            self.isInit = True

    def to_freetext(self):
        pass

    def to_data(self):
        pass

    def from_txt(self, creator: Creator):
        pass


class SaveManager:
    def __init__(self, base_path: str, formatter: Formatter = None) -> None:
        self.basePath = base_path
        self.formater = formatter

        if not os.path.exists(self.basePath):
            os.makedirs(self.basePath)

    def save_to_text(self, fileName: str, content: str) -> None:
        print(f"Saving: {self.basePath}/{fileName}.txt")

        with open(f"{self.basePath}/{fileName}.txt", "w") as f:
            f.write(content)

    def load_from_text(self, fileName: str) -> str:
        print(f"Saving: {self.basePath}/{fileName}.txt")

        with open(f"{self.basePath}/{fileName}.txt", "r") as f:
            content = f.read()

        return content
