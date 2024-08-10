#!/usr/bin/env python3
"""
Auth module for the API
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """
    Template for all authentication system
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if a given path requires authentication.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require
            authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from a Flask request object.

        Args:
            request (flask.Request, optional): The Flask request object.
            Defaults to None.

        Returns:
            str: The authorization header, or None if it is not present.
        """
        return None
        # if request is None:
        #     request = request

        # if 'Authorization' in request.headers:
        #     return request.headers['Authorization']
        # else:
        #     return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from a Flask request object.

        Args:
            request (flask.Request, optional): The Flask request object.
            Defaults to None.

        Returns:
            TypeVar('User'): The current user, or None if the user is
            not authenticated.
        """
        if request is None:
            request = request

        return None
