#!/usr/bin/env python3

from models.engine.file_storage import FileStorage

"""
    Module of __init__ that initialize the whole module.
"""


storage = FileStorage()
storage.reload()
