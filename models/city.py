#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Blueprint for City objects."""

    state_id = ""    # will be State.id
    name = ""
