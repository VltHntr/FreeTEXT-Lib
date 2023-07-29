from dataclasses import dataclass
import datetime

from FreeTEXTlib.Statics import LibraryInformation


@dataclass
class Creator:
    lastname: str
    firstname: str


@dataclass
class Header:
    creator: Creator
    date: str = str(datetime.date.today())


@dataclass
class Footer:
    libVersion: float = LibraryInformation.LIBVER.value
    programVersion: float = 0.1
    formatterVersion: float = LibraryInformation.FMTVER.value


@dataclass
class DataForm:
    header: Header
    body: str = ""
    footer: Footer = Footer()
