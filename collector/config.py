AGENT_DIRECTORY = 'agent/'
BIN_PATH = 'bin/'
CONF_PATH = 'conf/'
INSTALL_PATH = '/usr/local/logicmonitor/'

DEFAULT_OS = 'Linux'
TEMP_PATH = '/tmp/'

LOG_FILE = INSTALL_PATH + '/logs/wrapper.log'
COLLECTOR_LOCK = INSTALL_PATH + 'collector.found'

PARAM_OPTS = {
    'account': dict(required=True, default=None),
    'access_id': dict(required=True, default=None),
    'access_key': dict(required=True, default=None),

    'backup_collector_id': dict(required=False, default=None, type='int'),
    'collector_size': dict(
        required=False,
        default='small',
        choices=['nano', 'small', 'medium', 'large']
    ),
    'cleanup': dict(required=False, default=False, type='bool'),
    'collector_group': dict(required=False, default='/'),
    'collector_version': dict(required=False, default=None, type='int'),
    'description': dict(required=False, default=None),
    'enable_fail_back': dict(
        required=False,
        default=False,
        type='bool'
    ),
    'escalation_chain_id': dict(required=False, default=1, type='int'),
    'id': dict(required=False, default=None, type='int'),
    'resend_interval': dict(required=False, default=15, type='int'),
    'suppress_alert_clear': dict(
        required=False,
        default=False,
        type='bool'
    ),
    'use_ea': dict(
        required=False,
        default=False,
        type='bool'
    )
}