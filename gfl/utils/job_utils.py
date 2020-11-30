import time
import uuid

from gfl.conf import node_id


class JobUtils(object):

    def __init__(self):
        super(JobUtils, self).__init__()

    @classmethod
    def generate_job_id(cls):
        namespace = uuid.UUID(node_id[:32])
        nano_time = int(int(1e9) * time.time())
        name = node_id[32:] + str(nano_time / 100)
        return uuid.uuid3(namespace, name).hex
