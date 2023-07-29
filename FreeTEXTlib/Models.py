class Creator:
    def __init__(self, last_name: str, first_name: str) -> None:
        self.lastname = last_name
        self.firstname = first_name

    def get_lastname(self):
        return self.lastname

    def get_firstname(self):
        return self.firstname
