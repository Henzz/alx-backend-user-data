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
        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure path ends with a slash
        if not path.endswith('/'):
            path += '/'

        # Check if path is in excluded_paths
        for excluded_path in excluded_paths:
            # Ensure excluded_path ends with a slash
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            # Check if path matches the excluded_path
            if path == excluded_path or path.startswith(excluded_path):
                return False

        # Path is not in the list of excluded_paths,
        # so it requires authentication
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from a Flask request object.

        Args:
            request (flask.Request, optional): The Flask request object.
            Defaults to None.

        Returns:
            str: The authorization header, or None if it is not present.
        """
        if request is None:
            return None

        if 'Authorization' in request.headers:
            return request.headers['Authorization']
        else:
            return None

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
