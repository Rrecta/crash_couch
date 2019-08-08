# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class WorkflowCumulativeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, workflow_sid):
        """
        Initialize the WorkflowCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param workflow_sid: The workflow_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsList
        """
        super(WorkflowCumulativeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid, }

    def get(self):
        """
        Constructs a WorkflowCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        """
        return WorkflowCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            workflow_sid=self._solution['workflow_sid'],
        )

    def __call__(self):
        """
        Constructs a WorkflowCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        """
        return WorkflowCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            workflow_sid=self._solution['workflow_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowCumulativeStatisticsList>'


class WorkflowCumulativeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkflowCumulativeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param workflow_sid: The workflow_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsPage
        """
        super(WorkflowCumulativeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkflowCumulativeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        """
        return WorkflowCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            workflow_sid=self._solution['workflow_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowCumulativeStatisticsPage>'


class WorkflowCumulativeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, workflow_sid):
        """
        Initialize the WorkflowCumulativeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param workflow_sid: The workflow_sid

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        """
        super(WorkflowCumulativeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/CumulativeStatistics'.format(**self._solution)

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a WorkflowCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by an end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.
        :param unicode split_by_wait_time: A comma separated values for viewing splits of tasks canceled and accepted above the given threshold in seconds.

        :returns: Fetched WorkflowCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        """
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WorkflowCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            workflow_sid=self._solution['workflow_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowCumulativeStatisticsContext {}>'.format(context)


class WorkflowCumulativeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, workflow_sid):
        """
        Initialize the WorkflowCumulativeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        """
        super(WorkflowCumulativeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'avg_task_acceptance_time': deserialize.integer(payload['avg_task_acceptance_time']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'reservations_created': deserialize.integer(payload['reservations_created']),
            'reservations_accepted': deserialize.integer(payload['reservations_accepted']),
            'reservations_rejected': deserialize.integer(payload['reservations_rejected']),
            'reservations_timed_out': deserialize.integer(payload['reservations_timed_out']),
            'reservations_canceled': deserialize.integer(payload['reservations_canceled']),
            'reservations_rescinded': deserialize.integer(payload['reservations_rescinded']),
            'split_by_wait_time': payload['split_by_wait_time'],
            'wait_duration_until_accepted': payload['wait_duration_until_accepted'],
            'wait_duration_until_canceled': payload['wait_duration_until_canceled'],
            'tasks_canceled': deserialize.integer(payload['tasks_canceled']),
            'tasks_completed': deserialize.integer(payload['tasks_completed']),
            'tasks_entered': deserialize.integer(payload['tasks_entered']),
            'tasks_deleted': deserialize.integer(payload['tasks_deleted']),
            'tasks_moved': deserialize.integer(payload['tasks_moved']),
            'tasks_timed_out_in_workflow': deserialize.integer(payload['tasks_timed_out_in_workflow']),
            'workflow_sid': payload['workflow_sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'workflow_sid': workflow_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkflowCumulativeStatisticsContext for this WorkflowCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsContext
        """
        if self._context is None:
            self._context = WorkflowCumulativeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                workflow_sid=self._solution['workflow_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def avg_task_acceptance_time(self):
        """
        :returns: The average time from Task creation to acceptance
        :rtype: unicode
        """
        return self._properties['avg_task_acceptance_time']

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
    def reservations_created(self):
        """
        :returns: The total number of Reservations that were created for Workers
        :rtype: unicode
        """
        return self._properties['reservations_created']

    @property
    def reservations_accepted(self):
        """
        :returns: The total number of Reservations accepted by Workers
        :rtype: unicode
        """
        return self._properties['reservations_accepted']

    @property
    def reservations_rejected(self):
        """
        :returns: The total number of Reservations that were rejected
        :rtype: unicode
        """
        return self._properties['reservations_rejected']

    @property
    def reservations_timed_out(self):
        """
        :returns: The total number of Reservations that were timed out
        :rtype: unicode
        """
        return self._properties['reservations_timed_out']

    @property
    def reservations_canceled(self):
        """
        :returns: The total number of Reservations that were canceled
        :rtype: unicode
        """
        return self._properties['reservations_canceled']

    @property
    def reservations_rescinded(self):
        """
        :returns: The total number of Reservations that were rescinded
        :rtype: unicode
        """
        return self._properties['reservations_rescinded']

    @property
    def split_by_wait_time(self):
        """
        :returns: The splits of the tasks canceled and accepted based on the provided SplitByWaitTime parameter.
        :rtype: dict
        """
        return self._properties['split_by_wait_time']

    @property
    def wait_duration_until_accepted(self):
        """
        :returns: The wait duration stats for tasks that were accepted.
        :rtype: dict
        """
        return self._properties['wait_duration_until_accepted']

    @property
    def wait_duration_until_canceled(self):
        """
        :returns: The wait duration stats for tasks that were canceled.
        :rtype: dict
        """
        return self._properties['wait_duration_until_canceled']

    @property
    def tasks_canceled(self):
        """
        :returns: The total number of Tasks that were canceled
        :rtype: unicode
        """
        return self._properties['tasks_canceled']

    @property
    def tasks_completed(self):
        """
        :returns: The total number of Tasks that were completed
        :rtype: unicode
        """
        return self._properties['tasks_completed']

    @property
    def tasks_entered(self):
        """
        :returns: The total number of Tasks that entered this Workflow
        :rtype: unicode
        """
        return self._properties['tasks_entered']

    @property
    def tasks_deleted(self):
        """
        :returns: The total number of Tasks that were deleted
        :rtype: unicode
        """
        return self._properties['tasks_deleted']

    @property
    def tasks_moved(self):
        """
        :returns: The total number of Tasks that were moved from one queue to another
        :rtype: unicode
        """
        return self._properties['tasks_moved']

    @property
    def tasks_timed_out_in_workflow(self):
        """
        :returns: The total number of Tasks that were timed out of their Workflows
        :rtype: unicode
        """
        return self._properties['tasks_timed_out_in_workflow']

    @property
    def workflow_sid(self):
        """
        :returns: The workflow_sid
        :rtype: unicode
        """
        return self._properties['workflow_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a WorkflowCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by an end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.
        :param unicode split_by_wait_time: A comma separated values for viewing splits of tasks canceled and accepted above the given threshold in seconds.

        :returns: Fetched WorkflowCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workflow.workflow_cumulative_statistics.WorkflowCumulativeStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowCumulativeStatisticsInstance {}>'.format(context)
