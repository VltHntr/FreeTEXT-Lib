from dataclasses import dataclass
import datetime


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
    libVersion: float = 0.1
    programVersion: float = 0.1
    formatterVersion: float = 0.1


@dataclass
class DataForm:
    header: Header
    body: str = ""
    footer: Footer = Footer()
