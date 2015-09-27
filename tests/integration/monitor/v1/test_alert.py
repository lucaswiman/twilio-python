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


class AlertTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response({status}, {content}))
        self.twilio.monitor.v1.alerts()
        self.holodeck.assert_has_request(Request('get', 'https://monitor.twilio.com/v1/Alerts/{sid}'))
