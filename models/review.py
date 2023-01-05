#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Blueprint for Review objects."""

    place_id = ""    # will be the Place.id
    user_id = ""     # will be User.id
    text = ""
