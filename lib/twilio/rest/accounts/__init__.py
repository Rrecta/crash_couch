# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.accounts.v1 import V1


class Accounts(Domain):

    def __init__(self, twilio):
        """
        Initialize the Accounts Domain

        :returns: Domain for Accounts
        :rtype: twilio.rest.accounts.Accounts
        """
        super(Accounts, self).__init__(twilio)

        self.base_url = 'https://accounts.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of accounts
        :rtype: twilio.rest.accounts.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def credentials(self):
        """
        :rtype: twilio.rest.accounts.v1.credential.CredentialList
        """
        return self.v1.credentials

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts>'
