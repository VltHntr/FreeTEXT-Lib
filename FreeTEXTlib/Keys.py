from dataclasses import dataclass


@dataclass
class KeyCreator:
    lastname: str = "lastname"
    firstname: str = "firstname"


@dataclass
class Header:
    header: str = "header"
    creator: KeyCreator = KeyCreator()
    date: str = "date"


@dataclass
class Body:
    body: str = "body"


@dataclass
class Footer:
    libVersion: str = "libver"
    programVersion: str = "progver"
    formatterVersion: str = "fmtver"


@dataclass
class Keys:
    header: Header = Header()
    body: Body = Body()
    footer: Footer = Footer()
