"""
Style Guide for Python (PEP 8)
lowercase with words separated by underscores as necessary to improve readability.
"""

import datetime

class User:
    """ A member of FriendFace. For now we are
        only storing their name and birthday.
        But soon we will store an uncomfortable
        amount of user information.
    """

    # default initializer
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday    # yyyymmdd

        # extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """return the age of the user in years."""
        today = datetime.date.today()

        return today.year - int(self.birthday[0:4])


user1 = User("Dave Bowman", "19710315")
# user1.first_name = "Dave"
# user1.last_name = "Bowman"

print user1.first_name, user1.last_name

print user1.name, user1.age()

help(User)

# Help on class User in module __main__:
# class User
#  |  A member of FriendFace. For now we are
#  |  only storing their name and birthday.
#  |  But soon we will store an uncomfortable
#  |  amount of user information.
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, full_name, birthday)
#  |      # default initializer
#  |  
#  |  age(self)
#  |      return the age of the user in years.