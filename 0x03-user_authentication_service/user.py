#!/usr/bin/env python3
"""SQLAlchemy model for user
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the 'users' table.

    Attributes:
        id (int): Primary key.
        email (str): Email address (non-nullable).
        hashed_password (str): Hashed password (non-nullable).
        session_id (str): Session ID (nullable).
        reset_token (str): Password reset token (nullable).
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
