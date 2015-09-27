# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.conversations.v1.conversation.participant import ParticipantList


class CompletedList(ListResource):

    def __init__(self, version):
        """
        Initialize the CompletedList
        
        :param Version version: Version that contains the resource
        
        :returns: CompletedList
        :rtype: CompletedList
        """
        super(CompletedList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Conversations/Completed'.format(**self._kwargs)

    def stream(self, limit=None, page_size=None, **kwargs):
        """
        Streams CompletedInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            CompletedInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        """
        Reads CompletedInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of CompletedInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of CompletedInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            CompletedInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a CompletedContext
        
        :param sid: Contextual sid
        
        :returns: CompletedContext
        :rtype: CompletedContext
        """
        return CompletedContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.CompletedList>'


class CompletedContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the CompletedContext
        
        :param Version version
        :param sid: Contextual sid
        
        :returns: CompletedContext
        :rtype: CompletedContext
        """
        super(CompletedContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Conversations/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._participants = None

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
            )
        return self._participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.CompletedContext {}>'.format(context)


class CompletedInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CompletedInstance
        
        :returns: CompletedInstance
        :rtype: CompletedInstance
        """
        super(CompletedInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'status': payload['status'],
            'duration': deserialize.integer(payload['duration']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'account_sid': payload['account_sid'],
            'url': payload['url'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: CompletedContext for this CompletedInstance
        :rtype: CompletedContext
        """
        if self._instance_context is None:
            self._instance_context = CompletedContext(
                self._version,
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status
        :rtype: completed.status
        """
        return self._properties['status']

    @property
    def duration(self):
        """
        :returns: The duration
        :rtype: str
        """
        return self._properties['duration']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: str
        """
        return self._properties['url']

    @property
    def participants(self):
        """
        Access the participants
        
        :returns: participants
        :rtype: participants
        """
        return self._context.participants

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Conversations.V1.CompletedInstance {}>'.format(context)
