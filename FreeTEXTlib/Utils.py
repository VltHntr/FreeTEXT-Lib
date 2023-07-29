import json
import os

from FreeTEXTlib.Models import DataForm, Header, Creator
from FreeTEXTlib.Statics import Keys


class Formatter:
    data: DataForm

    def __init__(self) -> None:
        self.isInit = False

    def init_format(self, creator: Creator):
        if self.isInit:
            print("Already initialized...")
        else:
            print("initialize Formatter...")

            self.data = DataForm(
                header=Header(
                    creator=creator
                )
            )

            print("Formatter is initialized.")
            self.isInit = True

    def set_body(self, body: str):
        self.data.body = body

    def get_body(self):
        return self.data.body

    def overide_creator(self, new_creator: Creator):
        self.data.header.creator = new_creator

    def to_freetext(self):
        formatted = {
            Keys.header: {
                Keys.creator: {
                    Keys.lastName: self.data.header.creator.lastname,
                    Keys.firstName: self.data.header.creator.firstname
                },
                Keys.date: self.data.header.date
            },

            Keys.body: self.data.body,

            Keys.footer: {
                Keys.programVersion: self.data.footer.programVersion,
                Keys.libraryVersion: self.data.footer.libVersion,
                Keys.formatterVersion: self.data.footer.formatterVersion
            }
        }

        return json.dumps(formatted, indent=4)

    def to_data(self, data: str):
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
