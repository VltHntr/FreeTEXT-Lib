import json
import os

from FreeTEXTlib.Models import DataForm, Header, Creator, Footer
from FreeTEXTlib.Statics import Keys


class Formatter:
    data: DataForm
    error = "Please initialize rhe Formatter.\nThe DataClasses needs to initialize."

    def __init__(self, program_version: float) -> None:
        self.isInit = False
        self.progVersion = program_version

    def init_format(self, creator: Creator):
        if self.isInit:
            print("Already initialized...")
        else:
            print("initialize Formatter...")

            self.data = DataForm(
                header=Header(
                    creator=creator
                ),
                footer=Footer(programVersion=self.progVersion)
            )

            print("Formatter is initialized.")
            self.isInit = True

    def construct_new_data(self, header: Header, body: str, footer: Footer):
        self.set_header(header)
        self.set_body(body)
        self.set_footer(footer)

    def set_body(self, body: str):
        if self.isInit:
            self.data.body = body
        else:
            print(self.error)

    def get_body(self):
        if self.isInit:
            return self.data.body
        else:
            print(self.error)

    def set_header(self, new_header: Header):
        self.data.header = new_header

    def set_footer(self, new_footer: Footer):
        self.data.footer = new_footer

    def override_creator(self, new_creator: Creator):
        if self.isInit:
            self.data.header.creator = new_creator
        else:
            print(self.error)

    def to_freetext(self):
        if self.isInit:
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
        else:
            print(self.error)

    def to_data(self, data: str):
        pass

    def from_txt(self, creator: Creator):
        pass


class SaveManager:
    def __init__(self, base_path: str, formatter: Formatter = None) -> None:
        self.basePath = base_path
        self.formatter = formatter

        if not os.path.exists(self.basePath):
            os.makedirs(self.basePath)

    def save_to_text(self, file_name: str, content: str) -> None:
        print(f"Saving: {self.basePath}/{file_name}.txt")

        with open(f"{self.basePath}/{file_name}.txt", "w") as f:
            f.write(content)

    def load_from_text(self, file_name: str) -> str:
        print(f"Saving: {self.basePath}/{file_name}.txt")

        with open(f"{self.basePath}/{file_name}.txt", "r") as f:
            content = f.read()

        return content

    def save_to_freetxt(self, file_name: str):
        with open(f"{self.basePath}/{file_name}.freetxt", "w") as f:
            f.write(self.formatter.to_freetext())

        print(f"Saved to {file_name}.freetxt")

    def load_from_freetxt(self, file_name: str):
        with open(f"{self.basePath}/{file_name}.freetxt", "r") as f:
            raw_data = json.loads(f.read())

        header = Header(
            creator=Creator(raw_data[Keys.header][Keys.creator][Keys.lastName],
                            raw_data[Keys.header][Keys.creator][Keys.firstName]),
            date=raw_data[Keys.header][Keys.date]
        )

        body = raw_data[Keys.body]

        footer = Footer(
            programVersion=raw_data[Keys.footer][Keys.programVersion],
            libVersion=raw_data[Keys.footer][Keys.libraryVersion],
            formatterVersion=raw_data[Keys.footer][Keys.formatterVersion]
        )

        self.formatter.construct_new_data(header, body, footer)
        print(f"Loaded {file_name}.freetxt")
