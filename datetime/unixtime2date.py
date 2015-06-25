import time
import sys

if len(sys.argv) > 1:
    unixtime = sys.argv[1]
else:
    print("Please inform unixtime.")
    sys.exit(0)

time_struct = time.localtime(float(unixtime))

print("Date: {0}/{1}/{2}".format(
    time_struct.tm_mday, time_struct.tm_mon, time_struct.tm_year))
print("Hour: {0}:{1}:{2}".format(
    time_struct.tm_hour, time_struct.tm_min, time_struct.tm_sec))
