import gfl_test

import time

print(time.time())

from gfl.utils.job_utils import JobUtils

print(time.time())

if __name__ == "__main__":
    for i in range(10):
        print(JobUtils.generate_job_id())
        time.sleep(0.0000001)