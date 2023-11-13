class LibraryItem:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return True
        else:
            return False

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return True
        else:
            return False

    def display_info(self):
        status = 'Checked out' if self.checked_out else 'Available'
        return f"Title: {self.title}, Author: {self.author}, Date: {self.publication_date}, Status: {status}"


class Book(LibraryItem):
    def __init__(self, title, author, publication_date, isbn):
        super().__init__(title, author, publication_date)
        self.isbn = isbn

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, ISBN: {self.isbn}"


class DVD(LibraryItem):
    def __init__(self, title, author, publication_date, duration):
        super().__init__(title, author, publication_date)
        self.duration = duration

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, author, publication_date, category):
        super().__init__(title, author, publication_date)
        self.category = category

    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info}, Category: {self.category}"
