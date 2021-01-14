# Author: Vincent McIntosh
# Date: 10/28/20
# Description: Creates a Library simulator

class LibraryItem:
    """Creates a Library item, along with several methods"""

    def __init__(self, library_item_id, title):
        """Creates a Library item object with ID and title, while also initializing the following values"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_location(self):
        """Returns the item's location"""
        return self._location

    def get_library_item_id(self):
        """Returns the item ID"""
        return self._library_item_id

    def get_checked_out_by(self):
        """Returns who checked the item out"""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns who requested the item"""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns the date the item was checked out"""
        return self._date_checked_out

    def set_location(self, update):
        """Sets the item location"""
        self._location = update

    def set_checked_out_by(self, update):
        """Sets who checked the item out"""
        self._checked_out_by = update

    def set_requested_by(self, update):
        """Sets who requested the item"""
        self._requested_by = update

    def set_date_checked_out(self, update):
        """Sets the date the item was checked out"""
        self._date_checked_out = update


class Book(LibraryItem):
    """Creates a Book (inherited from LibraryItem)"""

    def __init__(self, library_item_id, title, author):
        """Creates a Book object with ID, title, and author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Returns book author"""
        return self._author

    def get_check_out_length(self):
        """Returns how long the book can be checked out"""
        length = 21
        return length

class Album(LibraryItem):
    """Creates an Album (inherited from LibraryItem)"""

    def __init__(self, library_item_id, title, artist):
        """Creates an album object with ID, title, and artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Returns album artist"""
        return self._artist

    def get_check_out_length(self):
        """Returns how long the album can be checked out"""
        length = 14
        return length

class Movie(LibraryItem):
    """Creates a Movie (inherited from LibraryItem)"""

    def __init__(self, library_item_id, title, director):
        """Creates a movie object with ID, title, and director"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Returns movie director"""
        return self._director

    def get_check_out_length(self):
        """Returns how long the movie can be checked out"""
        length = 7
        return length


class Patron:
    """Creates a Patron along with several methods"""

    def __init__(self, patron_id, name):
        """Creates a Patron object given ID and name"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = {}
        self._fine_amount = 0

    def get_fine_amount(self):
        """Returns the fine amount"""
        return self._fine_amount

    def add_library_item(self, item):
        """Adds the item to checked out items"""
        self._checked_out_items[item.get_library_item_id()] = item

    def remove_library_item(self, item):
        """Removes the item from collection of checked out items"""
        del self._checked_out_items[item]

    def get_checked_out_items(self):
        """Returns the collection of checked out items"""
        return self._checked_out_items

    def amend_fine(self, amount):
        """Changes the fine amount"""
        self._fine_amount = self._fine_amount + amount

    def get_patron_ID(self):
        """Returns the patron's ID"""
        return self._patron_id

class Library:
    """Creates a library, along with several methods"""

    def __init__(self):
        """Creates a Library object, initializing the date, holdings, and members"""
        self._current_date = 0
        self._holdings = {}
        self._members = {}

    def add_library_item(self, item):
        """Adds a library item to holdings"""
        self._holdings[item.get_library_item_id()] = item

    def add_patron(self, member):
        """Adds a patron to members"""
        self._members[member.get_patron_ID()] = member

    def get_library_item_from_id(self, ID):
        """Returns a library item given ID"""
        if ID in self._holdings:
            return self._holdings[ID]
        else:
            return None

    def get_patron_from_id(self, ID):
        """Returns a patron object given ID"""
        if ID in self._members:
            return self._members[ID]
        else:
            return None

    def check_out_library_item(self, patron, item):
        """Performs specified check out functions on a given library item"""
        if patron in self._members:
            if item in self._holdings:
                if self._holdings[item].get_location() == "CHECKED_OUT":
                    return "item already checked out"
                elif self._holdings[item].get_location() == "ON_HOLD_SHELF":
                    return "item on hold by other patron"
                else:
                    self._holdings[item].set_location("CHECKED_OUT")
                    self._holdings[item].set_date_checked_out(self._current_date)
                    self._holdings[item].set_checked_out_by(patron)
                    if self._holdings[item].get_requested_by == patron:
                        self._holdings[item].set_requested_by(None)
                    self._members[patron].add_library_item(self._holdings[item])
                    return "check out successful"
            else:
                return "item not found"
        else:
            return "patron not found"
        return "check out successful"

    def return_library_item(self, item):
        """Performs specified return functions on a given library item"""
        if item in self._holdings:
            if self._holdings[item].get_location() != "CHECKED_OUT":
                return "item already in library"
            else:
                member = self._holdings[item].get_checked_out_by()
                self._members[member].remove_library_item(item)
                if self._holdings[item].get_requested_by() != None:
                    self._holdings[item].set_location("ON_HOLD_SHELF")
                self._holdings[item].set_checked_out_by(None)
                return "return successful"
        else:
            return "item not found"

    def request_library_item(self, patron, item):
        """Performs several request functions given a patron and library item"""
        if patron in self._members:
            if item in self._holdings:
                if self._holdings[item].get_requested_by() != None:
                    return "item already on hold"
                else:
                    self._holdings[item].set_requested_by(patron)
                    if self._holdings[item].get_location() == "ON_SHELF":
                        self._holdings[item].set_location("ON_HOLD_SHELF")
                    return "request successful"
            else:
                return "item not found"
        else:
            return "patron not found"

    def pay_fine(self, patron, payment):
        """Reduces total fine amount given patron and payment"""
        if patron in self._members:
            amount = -(payment)
            self._members[patron].amend_fine(amount)
            return "payment successful"
        else:
            return "patron not found"

    def increment_current_date(self):
        """Increments the current date, and amends patron fines"""
        self._current_date += 1
        for patron in self._members:
            for item in self._members[patron].get_checked_out_items():
                if (self._current_date - self._holdings[item].get_date_checked_out()) > self._holdings[item].get_check_out_length():
                    self._members[patron].amend_fine(0.1)
