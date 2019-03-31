import platform
import uptime
from datetime import timedelta
import pyemtvlc


# Build uptime msg
def uptime_string():
    # Machine info
    uname = platform.uname()
    uptime_seconds = uptime.uptime()
    # Delta uptime in human readable format
    uptime_string = str(timedelta(seconds=uptime_seconds))
    # Build messsge
    string = ""
    string += "\U0001F4BB Running on " + uname[0] + " " + uname[2] + " " + uname[4] + "\n"
    string += "\U0000231B Uptime: " + uptime_string + "\n"
    return string


# Query EMT VLC and build msg
def query_emt(data):
    data_args = data.split()
    emt_info = pyemtvlc.next_buses(*data_args)
    return emt_info
