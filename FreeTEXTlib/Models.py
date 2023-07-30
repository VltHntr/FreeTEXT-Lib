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
    programVersion: float
    libVersion: float = LibraryInformation.LIBVER.value
    formatterVersion: float = LibraryInformation.FMTVER.value


@dataclass
class DataForm:
    header: Header
    footer: Footer
    body: str = ""
