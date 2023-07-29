class Creator:
    def __init__(self, LastName: str, FirstName: str) -> None:
        self.lastname = LastName
        self.firstname = FirstName

    def get_lastname(self):
        return self.lastname

    def get_firstname(self):
        return self.firstname
