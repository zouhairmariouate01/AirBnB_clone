#!/usr/bin/env python3

from models.base_model import BaseModel

"""
    User module.
    This modele contains a class of User.
"""


class User(BaseModel):
    """
        Class of User.
        To create a user instance, that has the next
        attributes:
            email, password, first_name and last_name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
