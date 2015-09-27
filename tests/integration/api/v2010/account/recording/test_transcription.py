# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class TranscriptionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response({status}, {content}))
        self.twilio.api.v2010.transcriptions()
        self.holodeck.assert_has_request(Request('get', 'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Recordings/{recording_sid}/Transcriptions/{sid}.json'))
