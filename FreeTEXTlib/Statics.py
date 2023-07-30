import dataclasses
from enum import Enum


class LibraryInformation(Enum):
    LIBVER = 0.1
    FMTVER = 0.1


@dataclasses.dataclass(frozen=True)
class Keys:
    header: str = "header"
    creator: str = "creator"
    lastName: str = "lastname"
    firstName: str = "firstname"
    date: str = "date"
    body: str = "body"
    footer: str = "footer"
    libraryVersion: str = "libver"
    programVersion: str = "progver"
    formatterVersion: str = "fmtver"


# This dict is just as a template and should not be used
v01 = {
    "header": {
        "creator": {
            "lastname": "",
            "firstname": ""
        },
        "date": ""
    },

    "body": "",

    "footer": {
        "libver": 0.1,
        "progver": 0.1,
        "fmtver": 0.1
    }
}
