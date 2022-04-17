from rvrbase import rvrlogger
from rvrbase import rvrconfig
from rvrbase import constants

# Log something.
thelogger = rvrlogger.Rvrlogger()
thelogger.log_application_event(
    type='warning', message='No worries, just testing here.')

# print something from the configuration file.
rvrconfig = rvrconfig.Rvrconfig(constants.CONFIG_FILE)
print(rvrconfig.q1('workspace_id'))
