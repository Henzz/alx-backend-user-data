#!/usr/bin/env python3
"""
Auth Basic module for the API
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Implements the Basic Authentication mechanism.
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header for a
        Basic Authentication.

        Args:
            authorization_header (str): The Authorization header to be checked.

        Returns:
            str: The Base64 part of the Authorization header, or None.
        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes a Base64 string.

        Args:
            base64_authorization_header (str): The Base64 string to be decoded.

        Returns:
            str: The decoded value as a UTF-8 string, or None.
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)\
                    .decode('utf-8')
            return decoded
        except (UnicodeDecodeError, base64.binascii.Error):
            return None
