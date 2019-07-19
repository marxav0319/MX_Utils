"""
This base mailer class serves as an abstract class for the implementation for various mailers.

Author: Mark Xavier
"""

from abc import ABC, abstractmethod

class Base_Mailer(ABC):
    """Non-instantiable.  This class serves as a base class for any children mailers."""

    def __init__(self, recipients, subject, body, signature):
        """Initializer for the base class."""

        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.signature = signature

    @abstractmethod
    def send(self):
        """
        """

        return
